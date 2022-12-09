import cv2
from multiprocessing import SimpleQueue


class ExamplePipeline:
    def __init__(self, data_queue: SimpleQueue, stream_queue: SimpleQueue):
        self.data_queue = data_queue
        self.stream_queue = stream_queue

        # TODO Construct pipes

    def process(self, image):
        if image is None:
            print('Pipeline: Received no image')
            return

        # TODO Run pipes
        # TODO Put data into queues
        self.data_queue.put('...')
        self.stream_queue.put('...')
