from multiprocessing import SimpleQueue

from apriltag.apriltag_params import AprilTagParams
from pipelines.base_pipeline import BasePipeline
from pipelines.apriltag_pipe import apriltag_pipe
from pipelines.draw_tags_pipe import draw_tags_pipe
from pipelines.grayscale_pipe import grayscale_pipe
from util.jetson_data import JetsonData
from util.math_util import matrix_to_quat


class AprilTagPipeline(BasePipeline):
    def __init__(self, data_queue: SimpleQueue, stream_queue: SimpleQueue):
        super().__init__(data_queue, stream_queue)

    def process(self, image, params, ts):
        if image is None:
            print('Pipeline: Received no image')
            return

        # GRAYSCALE PIPE
        gray_image = grayscale_pipe(image)

        # Run tag detection
        detections = apriltag_pipe(gray_image, AprilTagParams('tag16h5'), params.get_params_april())

        # DRAW TAGS PIPE
        output_image = draw_tags_pipe(gray_image, detections)

        if len(detections) > 0:
            for d in detections:
                output_data = JetsonData(
                    translation=(d.pose_t[0][0], d.pose_t[1][0], d.pose_t[2][0]),  # unpack tvec array
                    rotation=matrix_to_quat(d.pose_R),
                    ts=ts,
                    cid=params.cid,
                    tid=d.tag_id
                )
                self.data_queue.put(output_data)

        self.stream_queue.put(output_image)
