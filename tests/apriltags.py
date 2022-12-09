import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import cv2
from multiprocessing import SimpleQueue

from camera.camera_source import CameraSource
from pipelines.apriltag_pipeline import AprilTagPipeline


if __name__ == '__main__':
    data_queue = SimpleQueue()
    stream_queue = SimpleQueue()

    pipeline = AprilTagPipeline(data_queue, stream_queue)
    source = CameraSource('lifecamA_480p', pipeline)
    source.start()

    # Configure april tag pipeline (TODO read from REQ config file)
    # TODO pipeline.setDetectionParams(...)

    while True:
        # TODO: processing nanos, fps pipeline output
        print('pipeline data', data_queue.get())

        new_image = stream_queue.get()
        if new_image is not None:
            cv2.imshow('April Tag Output', new_image)

        # Terminate program on keystroke
        if cv2.waitKey(10) & 0xFF == ord('q'):
            print('Terminating...')
            break

    cv2.destroyAllWindows()
