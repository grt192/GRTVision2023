from multiprocessing import SimpleQueue
from camera.camera_params import CameraParams


class BasePipeline:
    """
    The base pipeline, initialized with a data and stream queue. The `CameraSource` that owns this pipeline
    periodically calls `process(image)` with a new frame of data.
    """
    def __init__(self, data_queue: SimpleQueue, stream_queue: SimpleQueue):
        self.data_queue = data_queue
        self.stream_queue = stream_queue

    def process(self, image, params: CameraParams, ts: int) -> None:
        """
        Processes a frame from a `CameraSource`. This method should `put()` data into the `data_queue`
        and `stream_queue` to queue it for broadcast to the correct destination.
        :param image: The image frame to process.
        :param params: The camera params of the invoking `CameraSource`.
        :param ts: The timestamp the image frame was captured at.
        """
        raise Exception('Not implemented!')
