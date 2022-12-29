import cv2
import time
from multiprocessing import Process, Queue
from camera.camera_params import CameraParams
from pipelines.base_pipeline import BasePipeline
from logger import init_process_logging


class CameraSource(Process):
    """
    A `CameraSource` process representing a camera on the jetson. `filename` should be a path to a camera
    config file (see `CameraParams`), and `pipelines` should be a list of pipelines this `CameraSource` owns
    (i.e. that this `CameraSource` sends frames to).
    """
    def __init__(self, filename: str, log_queue: Queue, *pipelines: BasePipeline):
        super().__init__()

        # Initialize objects
        self.cap = None
        self.frame = None

        # READ CONFIG FILE
        self.params = CameraParams(filename)

        # TODO: better way of passing around queues?
        self.logger = init_process_logging(log_queue)
        self.logger.info(f'Started Camera with id {self.params.cid}')

        self.pipelines = pipelines

    def run(self) -> None:
        while True:
            # Grab frame
            if self.cap is None or not self.cap.isOpened():
                self.cap = cv2.VideoCapture(self.params.path)  # , cv2.CAP_V4L)

            _, self.frame = self.cap.read()
            self.logger.debug(f'Frame received on CameraSource {self.params.cid}')
            ts = int(time.time() * 1000)  # Current time in ms

            # CALIBRATE IMAGE PIPE

            # RESIZE IMAGE PIPE

            # Send frame to pipelines for processing
            for pipeline in self.pipelines:
                pipeline.process(self.frame, self.params, self.logger, ts)

            time.sleep(1.0 / self.params.fps)
