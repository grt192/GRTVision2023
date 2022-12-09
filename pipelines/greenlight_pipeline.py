from multiprocessing import SimpleQueue
from .base_pipeline import BasePipeline


# takes in camera frames
# estimates the relative position from the camera to the target that reflects green
# outputs the relative position estimate of the green target from the camera as a tuple
# ex: (0, 1.5, 1)

class GreenLightPipeline(BasePipeline):
    def __init__(self, data_queue: SimpleQueue, stream_queue: SimpleQueue):
        super().__init__(data_queue, stream_queue)

        # TODO: init pipes

    def process(self, image, params):
        return
