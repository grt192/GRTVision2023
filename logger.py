import logging
import logging.handlers
import time
from multiprocessing import Queue


def init_process_logging(log_queue: Queue) -> logging.Logger:
    """
    Initializes logging on a process. This *must* be called for logging to work.
    :param log_queue: The `multiprocessing.Queue` that non-console logs should be broadcast to.
    :return: The configured `Logger` object.
    """
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    # Log INFO and above to console
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Log everything to logging process
    qh = logging.handlers.QueueHandler(log_queue)
    qh.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s - %(module)s %(levelname)s]: %(message)s')
    ch.setFormatter(formatter)
    qh.setFormatter(formatter)

    root.addHandler(ch)
    root.addHandler(qh)

    return root


# TODO: better name and combine with DS websocket process
def file_logger(log_queue: Queue) -> None:
    """
    A logger process that reads logs from a `log_queue` and writes them to a timestamped logfile.
    :param log_queue: The `multiprocessing.Queue` to read logs from.
    """
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    # Log everything to file
    fh = logging.FileHandler(f'vision.log.{int(time.time() * 1000)}')
    fh.setLevel(logging.DEBUG)

    root.addHandler(fh)

    while True:
        record = log_queue.get()
        logger = logging.getLogger(record.name)
        logger.handle(record)
