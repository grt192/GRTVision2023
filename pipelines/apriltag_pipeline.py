from multiprocessing import SimpleQueue

from apriltag.apriltag_params import AprilTagParams
from pipelines.base_pipeline import BasePipeline
from pipelines.apriltag_pipe import apriltag_pipe
from pipelines.draw_tags_pipe import draw_tags_pipe
from pipelines.grayscale_pipe import grayscale_pipe
from util.math_util import matrix_to_quat, quat_to_flu


class AprilTagPipeline(BasePipeline):
    def __init__(self, data_queue: SimpleQueue, stream_queue: SimpleQueue):
        super().__init__(data_queue, stream_queue)

    def process(self, image, params):
        if image is None:
            print('Pipeline: Received no image')
            return image, (False, [])

        # GRAYSCALE PIPE
        gray_image = grayscale_pipe(image)

        # Run tag detection
        detections = apriltag_pipe(gray_image, AprilTagParams('tag16h5'), params.get_params_april())

        # DRAW TAGS PIPE
        output_image = draw_tags_pipe(gray_image, detections)

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

