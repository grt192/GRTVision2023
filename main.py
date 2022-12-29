from multiprocessing import Process, SimpleQueue, Queue
from networker import networker
from pipelines.apriltag_pipeline import AprilTagPipeline
from pipelines.greenlight_pipeline import GreenLightPipeline
from camera.camera_source import CameraSource
from logger import file_logger


if __name__ == '__main__':
    data_queue = SimpleQueue()
    stream_queue = SimpleQueue()
    log_queue = Queue()

    sources = [
        CameraSource(  # Camera A
            "...",
            log_queue,
            GreenLightPipeline(data_queue, stream_queue),
            AprilTagPipeline(data_queue, stream_queue)
        ),
        CameraSource(  # Camera B
            "...",
            log_queue,
            AprilTagPipeline(data_queue, stream_queue)
        )
    ]

    networker_process = Process(target=networker, args=(data_queue, log_queue), daemon=True)
    networker_process.start()

    # Start `CameraSource` processes
    for source in sources:
        source.start()

    file_logger(log_queue)
