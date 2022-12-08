import cv2
from multiprocessing import Process

from apriltag.apriltag_pipe import AprilTagPipe
from apriltag.draw_tags_pipe import DrawTagsPipe
from generic_pipelines.grayscale_pipe import GrayscalePipe
from test_camera_source import TestCameraSource
from utils.math_utils import matrixToQuat, quatToFLU


class ExamplePipeline:
    def __init__(self, data_queue, stream_queue):
        self.data_queue = data_queue
        self.stream_queue = stream_queue

        # TODO Construct pipes

    def process(self, image):
        if image is None:
            print('Pipeline: Received no image')
            return

        # TODO Run pipes
        # TODO Put data into queues
