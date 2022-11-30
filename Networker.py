import time
import zmq

SERVER_IP = "tcp://localhost:5000"

context = zmq.Context()

print(f"Connecting a REQ client to {SERVER_IP}")
socket = context.socket(zmq.REQ)
socket.connect(SERVER_IP)

while True:
    # Send JSON data to RIO
    socket.send(b"{x: 3.5, y: 4.0, z: 1.203927}")

    time.sleep(1)

    message = socket.recv()
    print("Received reply %s" % message)
