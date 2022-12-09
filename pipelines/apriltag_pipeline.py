from multiprocessing import SimpleQueue

from base_pipeline import BasePipeline
from pipes.apriltag_pipe import AprilTagPipe
from pipes.draw_tags_pipe import DrawTagsPipe
from pipes.grayscale_pipe import GrayscalePipe
from util.math_util import matrix_to_quat, quat_to_flu


class AprilTagPipeline(BasePipeline):
    def __init__(self, data_queue: SimpleQueue, stream_queue: SimpleQueue):
        super().__init__(data_queue, stream_queue)

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
                output_r = quat_to_flu(matrix_to_quat(d.pose_R))
                output_t = (d.pose_t[0][0], d.pose_t[1][0], d.pose_t[2][0])  # unpack tvec array
                output_data[1].append((d.tag_id, output_r, output_t))

        self.data_queue.put(output_data)
        self.stream_queue.put(output_image)

