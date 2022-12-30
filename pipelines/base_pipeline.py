from multiprocessing import SimpleQueue
from camera.camera_params import CameraParams
from util.math_util import Translation, Quaternion
from util.jetson_data import JetsonData
from logging import Logger


class BasePipeline:
    """
    The base pipeline, initialized with a data and stream queue and `CameraSource`-specific parameters. The
    `CameraSource` that owns this pipeline periodically calls `process(image)` with new frames of data.
    """
    def __init__(self, data_queue: SimpleQueue, stream_queue: SimpleQueue, params: CameraParams, logger: Logger):
        self.data_queue = data_queue
        self.stream_queue = stream_queue

        self.params = params
        self.logger = logger

    def process(self, image, ts: int) -> None:
        """
        Processes a frame from a `CameraSource`. This method should call `_broadcast_data()` with data to send it
        to the RIO.
        :param image: The image frame to process.
        :param ts: The timestamp the image frame was captured at.
        """
        raise Exception('Not implemented!')

    def _broadcast_data(self, translation: Translation, rotation: Quaternion, ts: int, tid: int) -> None:
        """
        Queues data to be broadcast to the RIO.
        :param translation: The translation `(x, y, z)` of the target relative to the camera.
        :param rotation: The quaternion rotation `(w, x, y, z) of the target relative to the camera.
        :param ts: The `CameraSource` provided timestamp of the camera frame.
        :param tid: The id of the target (0-29 for AprilTags, 30+ for custom targets).
        """
        self.data_queue.put(JetsonData(translation, rotation, ts, tid, self.params.cid))
