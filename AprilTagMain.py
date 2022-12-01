# Tester script for AprilTagPipeline
from apriltag.AprilTagPipeline import AprilTagPipeline
from camera.CameraSource import CameraSource

if __name__ == '__main__':
    pipeline = AprilTagPipeline()
    source = CameraSource('webcam_1080p')

    # Configure april tag pipeline (TODO read from REQ config file)
    # TODO pipeline.setDetectionParams(...)
    pipeline.setCameraParams(source.params.getParamsApril())

    while True:
        # TODO: processing nanos, fps pipeline output
        data, new_image = pipeline.process(source.get_frame())
        print(data)
        cv2.imshow('April Tag Output', new_image)

        # Terminate program on keystroke
        if cv2.waitKey(0):
            break
    
    cv2.destroyAllWindows()
