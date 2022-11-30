import time
import zmq

SERVER_IP = "tcp://*:5000"

context = zmq.Context()

print(f"Connecting a PUB server to {SERVER_IP}")
socket = context.socket(zmq.PUB)
socket.bind(SERVER_IP)

while True:
    # Send JSON data to RIO
    data = "{x: 3.5, y: 4.0, z: 1.203927}"
    print(f"Sending data: {data}")
    socket.send_string(data)

    time.sleep(1)
