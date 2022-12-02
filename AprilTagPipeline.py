from apriltag.AprilTagPipe import AprilTagPipe
from apriltag.DrawTagsPipe import DrawTagsPipe
from pipe.GrayscalePipe import GrayscalePipe
from camera.CameraSource import CameraSource
from utils.MathUtils import matrixToQuat, quatToFLU

import cv2

class AprilTagPipeline:
    def __init__(self):
        
        # Sub-pipelines
        self.grayscalePipe = GrayscalePipe()
        self.aprilTagPipe = AprilTagPipe()
        self.drawTagsPipe = DrawTagsPipe()

    # Output: image, data is tuple of BOOL (data exists or not) and DATA ARRAY
    def run(self, image):

        if image is None:
            print('Pipeline: Received no image')
            return image, (False, [])

        # GRAYSCALE PIPE
        gray_image = self.grayscalePipe.process(image)

        # Run tag detection
        detections = self.aprilTagPipe.process(gray_image)

        # DRAW TAGS PIPE
        output_image = self.drawTagsPipe.process(gray_image, detections)
        
        if len(detections) == 0:
            output_data = (False, [])
        else:
            # Construct output data
            output_data = (True, [])
            for d in detections:
                output_r = quatToFLU(matrixToQuat(d.pose_R))
                output_t = (d.pose_t[0][0], d.pose_t[1][0], d.pose_t[2][0]) # unpack tvec array
                output_data[1].append((d.tag_id, output_r, output_t))

        return output_image, output_data


if __name__ == '__main__':
    pipeline = AprilTagPipeline()
    source = CameraSource('lifecamA_480p')

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
