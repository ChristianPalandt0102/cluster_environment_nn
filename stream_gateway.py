# stream_gateway.py

import asyncio
import json
import websockets


class StreamGateway:

    def __init__(self):
        self.feeds = {}
        self.data_buffer = []

    async def connect(self, name, url):

        async with websockets.connect(url) as ws:

            self.feeds[name] = ws

            while True:
                msg = await ws.recv()

                try:
                    data = json.loads(msg)
                except:
                    data = {"raw": msg}

                self.data_buffer.append({
                    "source": name,
                    "data": data
                })

    def get_latest(self):
        return self.data_buffer[-10:] if self.data_buffer else []