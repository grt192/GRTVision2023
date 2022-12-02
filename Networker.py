import json
from random import Random
import time
import zmq

LOCAL_DEBUG = True
SERVER_IP = "tcp://*:5000" if LOCAL_DEBUG else "tcp://10.1.92.94:5000"
RIO_IDENT = b"RIO"

context = zmq.Context()

print(f"Connecting a ROUTER to {SERVER_IP}")
socket = context.socket(zmq.ROUTER)
socket.bind(SERVER_IP)

random = Random()

while True:
    data = {
        "x": 12.12507 * random.random(),
        "y": 3.2394682 * random.random(),
        "z": 5.238 * random.random(),
        "ts": int(time.time() * 1000)  # Current time in ms
    }

    # Poll socket for inbound messages
    if socket.poll(0):
        RIO_IDENT = socket.recv()  # Store the identity payload in case the RIO has reconnected
        print(f"Received: {socket.recv_string()}")

    # Send JSON data to RIO
    message = json.dumps(data)
    print(f"Sending data: {message}")
    socket.send(RIO_IDENT, flags=zmq.SNDMORE)  # Prefix with RIO identity string
    socket.send_string(message)

    time.sleep(0.01)
