from multiprocessing import Process, SimpleQueue
from networker import networker
from pipelines.apriltag_pipeline import AprilTagPipeline
from pipelines.greenlight_pipeline import GreenLightPipeline
from localization import Localization
from camera.camera_source import CameraSource


if __name__ == '__main__':
    data_queue = SimpleQueue()
    stream_queue = SimpleQueue()

    sources = [
        CameraSource(0, 0, 0, 1, 0, 0, 0)  # Turret camera
    ]

    green_pipeline = GreenLightPipeline()
    april_pipeline = AprilTagPipeline()

    # localizer = Localization()

    networker_process = Process(target=networker, args=(data_queue,), daemon=True)
    networker_process.start()

    while True:
        for source in sources:
            frame = source.get_frame()
            green_pipeline.get(frame)
            april_pipeline.run(frame)
