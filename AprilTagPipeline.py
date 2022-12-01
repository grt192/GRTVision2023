from apriltag.AprilTagPipe import AprilTagPipe
from apriltag.DrawTagsPipe import DrawTagsPipe
from pipe.GrayscalePipe import GrayscalePipe
from camera.CameraSource import CameraSource

class AprilTagPipeline:
    def __init__(self):
        
        # Sub-pipelines
        self.grayscalePipe = GrayscalePipe()
        self.aprilTagPipe = AprilTagPipe()
        self.drawTagsPipe = DrawTagsPipe()

    def run(self, image):
        # GRAYSCALE PIPE
        gray_image = self.grayscalePipe.process(image)

        # Run tag detection
        detections = self.aprilTagPipe(gray_image)

        # DRAW TAGS PIPE
        output_image = self.drawTagsPipe.process(image, detections)
        
        # Construct output data
        output_data = []
        for d in detections:
            output_data.append((d.tag_id, d.pose_R, d.pose_t))

        return output_image, output_data


if __name__ == '__main__':
    pipeline = AprilTagPipeline()
    source = CameraSource('webcam_1080p')

    # Configure april tag pipeline (TODO read from REQ config file)
    # TODO pipeline.setDetectionParams(...)
    pipeline.aprilTagPipe.setCameraParams(source.params.getParamsApril())

    while True:
        # TODO: processing nanos, fps pipeline output
        new_image, data = pipeline.run(source.get_frame())
        print(data)
        cv2.imshow('April Tag Output', new_image)

        # Terminate program on keystroke
        if cv2.waitKey(0):
            break
    
    cv2.destroyAllWindows()
