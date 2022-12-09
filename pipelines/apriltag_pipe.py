from typing import Tuple

from pupil_apriltags import Detector
from apriltag.apriltag_params import AprilTagParams


# lower resolution tag family Tag16h5 teams should be able to detect the tags from further away for a given
# resolution and use a little less CPU doing so (or process at a higher frame rate) trade-off is an increase in false
# detections, mitigated by using an appropriate minimum size and more aggressively rejecting tags with bit errors
# https://www.chiefdelphi.com/t/frc-blog-2023-approved-devices-rules-preview-and-vision-target-update/417253

# tag PDF source: https://github.com/TylerSeiford/apriltag-pdfs

detector = None


def apriltag_pipe(image, detection_params: AprilTagParams, camera_params: Tuple[float, float, float, float]):
    global detector
    if detector is None:
        detector = Detector(
            families=detection_params.tag_family,
            nthreads=detection_params.n_threads,
            quad_decimate=detection_params.quad_decimate,
            quad_sigma=detection_params.quad_sigma,
            refine_edges=detection_params.refine_edges,
            decode_sharpening=detection_params.decode_sharpening,
            debug=detection_params.debug
        )

    # Run tag detection
    detections = detector.detect(
        image,
        estimate_tag_pose=True,
        camera_params=camera_params,
        tag_size=detection_params.tag_size
    )

    return detections
