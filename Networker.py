import json
from random import Random
import time
import zmq

SERVER_IP = "tcp://*:5000"

context = zmq.Context()

print(f"Connecting a PUB server to {SERVER_IP}")
socket = context.socket(zmq.PUB)
socket.bind(SERVER_IP)

random = Random()

while True:
    data = {
        "x": 12.12507 * random.random(),
        "y": 3.2394682 * random.random(),
        "z": 5.238 * random.random(),
        "ts": time.time_ns() // 1000000  # Current time in ms
    }

    # Send JSON data to RIO
    message = json.dumps(data)
    print(f"Sending data: {message}")
    socket.send_string(message)

    time.sleep(0.01)
