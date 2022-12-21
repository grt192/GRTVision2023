from multiprocessing import Process, SimpleQueue
from networker import networker
from pipelines.apriltag_pipeline import AprilTagPipeline
from pipelines.greenlight_pipeline import GreenLightPipeline
from camera.camera_source import CameraSource


if __name__ == '__main__':
    data_queue = SimpleQueue()
    stream_queue = SimpleQueue()

    sources = [
        CameraSource(  # Camera A
            "...",
            GreenLightPipeline(data_queue, stream_queue),
            AprilTagPipeline(data_queue, stream_queue)
        ),
        CameraSource(  # Camera B
            "...",
            AprilTagPipeline(data_queue, stream_queue)
        )
    ]

    # networker_process = Process(target=networker, args=(data_queue,), daemon=True)
    # networker_process.start()

    # Start `CameraSource` processes
    for source in sources:
        source.start()

    networker(data_queue)
