from multiprocessing import Process, SimpleQueue
from networker import networker
from pipelines.apriltag_pipeline import AprilTagPipeline
from pipelines.greenlight_pipeline import GreenLightPipeline
from localization import Localization
from camera.camera_source import CameraSource


if __name__ == '__main__':
    data_queue = SimpleQueue()
    stream_queue = SimpleQueue()

    green_pipeline = GreenLightPipeline(data_queue, stream_queue)
    april_pipeline = AprilTagPipeline(data_queue, stream_queue)

    sources = [
        CameraSource(  # Turret camera
            "...",
            green_pipeline,
            april_pipeline
        )
    ]

    # localizer = Localization()

    # networker_process = Process(target=networker, args=(data_queue,), daemon=True)
    # networker_process.start()

    # Start `CameraSource` processes
    for source in sources:
        source.start()

    networker(data_queue)
