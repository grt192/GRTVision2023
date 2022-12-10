from random import Random
import time
import zmq
from multiprocessing import Process, SimpleQueue
from util.jetson_data import JetsonData

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
        message = data_queue.get().to_json_str()
        print(f"Sending data: {message}")
        socket.send_string(message)


if __name__ == '__main__':
    random = Random()
    data_queue = SimpleQueue()

    networker_process = Process(target=networker, args=(data_queue,), daemon=True)
    networker_process.start()

    # Test the networker by continually sending semi-random data
    while True:
        data = JetsonData(
            translation=(1.0 * random.random(), 1.5 * random.random(), 2.4 * random.random()),
            rotation=(1.0 * random.random(), 1.0 * random.random(), 1.0 * random.random(), 1.0 * random.random()),
            ts=int(time.time() * 1000),  # Current time in ms
            tid=16,
            cid=3
        )
        data_queue.put(data)
        time.sleep(0.01)
