# core_kernel.py

import time
from threading import Lock

class CoreKernel:

    def __init__(self):
        self.nodes = {}
        self.state = "BOOT"
        self.lock = Lock()

    def register_node(self, name, obj):
        with self.lock:
            self.nodes[name] = obj

    def broadcast(self, signal):
        for n in self.nodes.values():
            if hasattr(n, "receive_signal"):
                n.receive_signal(signal)

    def heartbeat(self):
        while True:
            self.broadcast({"type": "heartbeat"})
            time.sleep(1)

kernel = CoreKernel()