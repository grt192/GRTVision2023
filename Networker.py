import json
from random import Random
import time
import zmq
from multiprocessing import Process, SimpleQueue

LOCAL_DEBUG = True
SERVER_IP = "tcp://*:5000" if LOCAL_DEBUG else "tcp://10.1.92.94:5000"
RIO_IDENT = b"RIO"


# A networker that sends and receives data from the RoboRIO over a ROUTER/DEALER socket.
# Data is queued to be sent via the `data_queue`, and is broadcast as fast as it arrives.
def networker(data_queue: SimpleQueue):
    context = zmq.Context()

    print(f"Connecting a ROUTER to {SERVER_IP}")
    socket = context.socket(zmq.ROUTER)
    socket.bind(SERVER_IP)

    while True:
        # Poll socket for inbound messages
        if socket.poll(0):
            socket.recv()  # Skip the identity frame
            print(f"Received: {socket.recv_string()}")

        # If there's data in the queue, send it to the RIO
        if not data_queue.empty():
            message = json.dumps(data_queue.get())
            print(f"Sending data: {message}")
            socket.send(RIO_IDENT, flags=zmq.SNDMORE)  # Prefix with RIO identity frame
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
