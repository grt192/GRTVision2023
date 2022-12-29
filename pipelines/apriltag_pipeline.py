from apriltag.apriltag_params import AprilTagParams
from pipelines.base_pipeline import BasePipeline
from pipelines.apriltag_pipe import apriltag_pipe
from pipelines.draw_tags_pipe import draw_tags_pipe
from pipelines.grayscale_pipe import grayscale_pipe
from util.math_util import matrix_to_quat
from logger import logger


class AprilTagPipeline(BasePipeline):
    def process(self, image, params, ts):
        if image is None:
            logger.warning('Received no image')
            return

        # GRAYSCALE PIPE
        gray_image = grayscale_pipe(image)

        # Run tag detection
        detections = apriltag_pipe(gray_image, AprilTagParams('tag16h5'), params.get_params_april())
        logger.info(f'Received {len(detections)} detections')

        # DRAW TAGS PIPE
        output_image = draw_tags_pipe(gray_image, detections)

        for d in detections:
            self._broadcast_data(
                translation=(d.pose_t[0][0], d.pose_t[1][0], d.pose_t[2][0]),  # unpack tvec array
                rotation=matrix_to_quat(d.pose_R),
                ts=ts,
                cid=params.cid,
                tid=d.tag_id
            )

        self.stream_queue.put(output_image)
