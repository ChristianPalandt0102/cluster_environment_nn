# observer_ws_stream.py

import asyncio
import json
import websockets


class ObserverStream:

    def __init__(self, observer, host="0.0.0.0", port=8765):
        self.observer = observer
        self.host = host
        self.port = port
        self.clients = set()

    async def handler(self, websocket):
        self.clients.add(websocket)
        try:
            while True:
                snapshot = self.observer.snapshot()
                await websocket.send(json.dumps(snapshot))
                await asyncio.sleep(2)
        finally:
            self.clients.remove(websocket)

    async def start(self):
        server = await websockets.serve(
            self.handler,
            self.host,
            self.port
        )

        print(f"[OBSERVER STREAM] ws://{self.host}:{self.port}")
        await server.wait_closed()


def run_stream(observer):
    stream = ObserverStream(observer)
    asyncio.run(stream.start())