import asyncio, json, websockets

class StreamGateway:

    def __init__(self):
        self.buffer = []

    async def connect(self, name, url):
        async with websockets.connect(url) as ws:
            while True:
                msg = await ws.recv()
                try:
                    data = json.loads(msg)
                except:
                    data = {"raw": msg}

                self.buffer.append({"source": name, "data": data})

    def get_latest(self):
        return self.buffer[-10:]