from multiprocessing import SimpleQueue


# takes in camera frames
# estimates the relative position from the camera to the target that reflects green
# outputs the relative position estimate of the green target from the camera as a tuple
# ex: (0, 1.5, 1)

class GreenLightPipeline:
    def __init__(self, data_queue: SimpleQueue, stream_queue: SimpleQueue):
        self.data_queue = data_queue
        self.stream_queue = stream_queue

    def process(self, image):
        return
