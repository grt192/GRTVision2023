from pupil_apriltags import Detector

# lower resolution tag family Tag16h5 
# teams should be able to detect the tags from further away for a given resolution and use a little less CPU doing so (or process at a higher frame rate)
# trade-off is an increase in false detections, mitigated by using an appropriate minimum size and more aggressively rejecting tags with bit errors 
# https://www.chiefdelphi.com/t/frc-blog-2023-approved-devices-rules-preview-and-vision-target-update/417253

# tag PDF source: https://github.com/TylerSeiford/apriltag-pdfs

class AprilTagPipe:


    def __init__(self):
        
        # Default detection params
        self.TAG_SIZE = 0.200 # in meters

        self.TAG_FAMILY = 'tag16h5'
        self.N_THREADS = 1
        self.DECIMATE = 1.0
        self.SIGMA_BLUR = 0.0
        self.REFINE_EDGES = 1
        self.DECODE_SHARPENING = 0.25
        self.DEBUG = 0

        self.detector = Detector(
            families=self.TAG_FAMILY,
            nthreads=self.N_THREADS,
            quad_decimate=self.DECIMATE,
            quad_sigma=self.SIGMA_BLUR,
            refine_edges=self.REFINE_EDGES,
            decode_sharpening=self.DECODE_SHARPENING,
            debug=self.DEBUG,
        )
        
        # Default camera params [fx, fy, cx, cy]  
        self.CAMERA_PARAMS = (0, 0, 0, 0)

    
    # Receives gray image, returns detections
    def get(self, image):
        # Run tag detection
        detections = self.detector.detect(gray_image, estimate_tag_pose=True, camera_params=self.CAMERA_PARAMS, tag_size=self.TAG_SIZE)

        return detections


    # Re-initializes detector with parameters as defined by class variables
    def updateDetector(self):
        self.detector = Detector(
            families=self.TAG_FAMILY,
            nthreads=self.N_THREADS,
            quad_decimate=self.DECIMATE,
            quad_sigma=self.SIGMA_BLUR,
            refine_edges=self.REFINE_EDGES,
            decode_sharpening=self.DECODE_SHARPENING,
            debug=self.DEBUG,
        )


    def setDetectionParams(self, tag_size, tag_family, n_threads, decimate, sigma_blur, refine_edges, decode_sharpening, debug):
        self.TAG_SIZE = tag_size

        self.TAG_FAMILY = tag_family
        self.N_THREADS = n_threads
        self.DECIMATE = decimate
        self.SIGMA_BLUR = sigma_blur
        self.REFINE_EDGES = refine_edges
        self.DECODE_SHARPENING = decode_sharpening
        self.DEBUG = debug

        updateDetector()

    def setCameraParams(self, params):
        self.CAMERA_PARAMS = params 