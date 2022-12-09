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
        CameraSource("...")  # Turret camera
    ]

    green_pipeline = GreenLightPipeline(data_queue, stream_queue)
    april_pipeline = AprilTagPipeline(data_queue, stream_queue)

    # localizer = Localization()

    networker_process = Process(target=networker, args=(data_queue,), daemon=True)
    networker_process.start()

    while True:
        for source in sources:
            frame = source.get_frame()
            green_pipeline.process(frame)
            april_pipeline.process(frame)
