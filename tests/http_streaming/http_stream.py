import os
import socket
import asyncio, websockets
import threading, time
from flask import Flask, send_file

curr_dir = os.path.dirname(os.path.abspath(__file__))
CONNECTIONS = set()

# async def handler(websocket):
    # name = await websocket.recv()
    # print(f"<<< {name}")

    # greeting = f"Hello {name}!"

    # await websocket.send(greeting)
    # print(f">>> {greeting}")

async def handler(websocket):
    CONNECTIONS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def websockmain():
    async with websockets.serve(handler, "127.0.0.1", 50001):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 49999))

    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return send_file("test.html")

    @app.route("/jmuxer.min.js")
    def jmuxer():
        return send_file("jmuxer.min.js")

    flask_thread = threading.Thread(target=lambda: app.run(port=50000, debug=False, threaded=True))
    flask_thread.daemon = True
    flask_thread.start()

    websock_thread = threading.Thread(target=lambda: asyncio.run(websockmain()))
    websock_thread.daemon = True
    websock_thread.start()
    # asyncio.run(websockmain())

    while True:
        data, addr = sock.recvfrom(99999)
        # print(data)
        websockets.broadcast(CONNECTIONS, data)