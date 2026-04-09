# sandbox_grid_engine.py

import asyncio
import uuid
import time
from collections import deque

MBIT_BUFFER_LIMIT = 1024 * 1024 * 8   # ~8MB safety


class Signal:
    def __init__(self, source, target, payload, signal_type="data"):
        self.id = str(uuid.uuid4())
        self.source = source
        self.target = target
        self.payload = payload
        self.type = signal_type
        self.timestamp = time.time()


class SandboxGridEngine:

    def __init__(self, router=None, cortex=None):
        self.router = router
        self.cortex = cortex

        self.boxes = {}
        self.signal_queue = deque()
        self.buffer_size = 0

        self.running = False

    # -----------------------------
    # Register sandbox
    # -----------------------------
    def register_box(self, name, handler):
        self.boxes[name] = handler
        print(f"[GRID] registered {name}")

    # -----------------------------
    # Emit Signal
    # -----------------------------
    def emit(self, source, target, payload, signal_type="data"):

        signal = Signal(source, target, payload, signal_type)

        size = len(str(payload).encode())

        if self.buffer_size + size > MBIT_BUFFER_LIMIT:
            print("[GRID] buffer overflow prevented")
            return False

        self.signal_queue.append(signal)
        self.buffer_size += size
        return True

    # -----------------------------
    # Routing Loop
    # -----------------------------
    async def dispatcher(self):

        self.running = True

        while self.running:

            if not self.signal_queue:
                await asyncio.sleep(0.01)
                continue

            signal = self.signal_queue.popleft()
            self.buffer_size -= len(str(signal.payload))

            await self.route(signal)

    # -----------------------------
    async def route(self, signal):

        if signal.target in self.boxes:
            await self.boxes[signal.target](signal)

        elif self.router:
            route = self.router.choose_route(
                {"type": signal.type},
                [{"name": k, "health": 1.0} for k in self.boxes]
            )
            await self.boxes[route["name"]](signal)

        if self.cortex:
            self.cortex.remember(signal.source, signal.type)