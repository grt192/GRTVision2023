import json
from random import Random
import time
import zmq
from multiprocessing import Process, SimpleQueue

LOCAL_DEBUG = False
SERVER_IP = "tcp://*:5800" if LOCAL_DEBUG else "tcp://10.1.92.94:5800"
RIO_IDENT = b"RIO"


# A networker that sends data to the RoboRIO over a PUB/SUB connection.
# Data is queued to be sent via the `data_queue`, and is broadcast as fast as it arrives.
def networker(data_queue: SimpleQueue):
    context = zmq.Context()

    print(f"Connecting a PUB server to {SERVER_IP}")
    socket = context.socket(zmq.PUB)
    socket.bind(SERVER_IP)

    # While the process is running, wait for messages in the queue and send them.
    while True:
        message = json.dumps(data_queue.get())
        # print(f"Sending data: {message}")
        socket.send_string(message)


if __name__ == '__main__':
    random = Random()
    data_queue = SimpleQueue()

    networker_process = Process(target=networker, args=(data_queue,), daemon=True)
    networker_process.start()

    # Test the networker by continually sending semi-random data
    while True:
        data = {
            "x": 12.12507 * random.random(),
            "y": 3.2394682 * random.random(),
            "z": 5.238 * random.random(),
            "ts": int(time.time() * 1000)  # Current time in ms
        }
        data_queue.put(data)
        time.sleep(0.01)
