from multiprocessing import Process

from apriltag.apriltag_pipe import AprilTagPipe
from apriltag.draw_tags_pipe import DrawTagsPipe
from generic_pipelines.grayscale_pipe import GrayscalePipe
from test_camera_source import TestCameraSource
from utils.math_utils import matrixToQuat, quatToFLU

import cv2

class AprilTagPipeline:
    def __init__(self, data_queue, stream_queue):
        self.data_queue = data_queue
        self.stream_queue = stream_queue

        # Sub-pipelines
        self.grayscale_pipe = GrayscalePipe()
        self.apriltag_pipe = AprilTagPipe()
        self.drawtags_pipe = DrawTagsPipe()

    # Output: image, data is tuple of BOOL (data exists or not) and DATA ARRAY
    def process(self, image):

        if image is None:
            print('Pipeline: Received no image')
            return image, (False, [])

        # GRAYSCALE PIPE
        gray_image = self.grayscale_pipe.process(image)

        # Run tag detection
        detections = self.apriltag_pipe.process(gray_image)

        # DRAW TAGS PIPE
        output_image = self.drawtags_pipe.process(gray_image, detections)
        
        if len(detections) == 0:
            output_data = (False, [])
        else:
            # Construct output data
            output_data = (True, [])
            for d in detections:
                output_r = quatToFLU(matrixToQuat(d.pose_R))
                output_t = (d.pose_t[0][0], d.pose_t[1][0], d.pose_t[2][0]) # unpack tvec array
                output_data[1].append((d.tag_id, output_r, output_t))

        data_queue.put(output_data)
        stream_queue.put(output_image)


if __name__ == '__main__':
    pipeline = AprilTagPipeline()
    source = TestCameraSource('lifecamA_480p')

    # Configure april tag pipeline (TODO read from REQ config file)
    # TODO pipeline.setDetectionParams(...)
    pipeline.aprilTagPipe.setCameraParams(source.params.getParamsApril())

    while True:
        # TODO: processing nanos, fps pipeline output
        new_image, data = pipeline.run(source.get_frame())
        print('pipeline data', data)
        
        if new_image is not None:
            cv2.imshow('April Tag Output', new_image)

        # Terminate program on keystroke
        if cv2.waitKey(10) & 0xFF == ord('q'):
            print('Terminating...')
            break
        
    
    cv2.destroyAllWindows()
