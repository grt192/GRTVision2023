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
            filename="...",
            data_queue=data_queue,
            stream_queue=stream_queue,
            log_queue=log_queue,
            pipelines=(GreenLightPipeline, AprilTagPipeline)  # TODO: not sure why this gives a type warning but the below doesn't
        ),
        CameraSource(  # Camera B
            filename="...",
            data_queue=data_queue,
            stream_queue=stream_queue,
            log_queue=log_queue,
            pipelines=(AprilTagPipeline,)
        )
    ]

    networker_process = Process(target=networker, args=(data_queue, log_queue), daemon=True)
    networker_process.start()

    # Start `CameraSource` processes
    for source in sources:
        source.start()

    file_logger(log_queue)
