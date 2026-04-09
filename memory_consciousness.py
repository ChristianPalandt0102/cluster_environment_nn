# memory_consciousness.py

import json
from pathlib import Path
import time

MEMORY_FILE = Path("collective_memory.json")


class DistributedMemory:

    def __init__(self):
        self.memory = {"events": [], "knowledge": {}}
        self.load()

    def remember(self, source, signal):
        self.memory["events"].append({
            "time": time.time(),
            "source": source,
            "signal": signal
        })
        self.save()

    def learn(self, key, value):
        self.memory["knowledge"][key] = value
        self.save()

    def recall(self, key):
        return self.memory["knowledge"].get(key)

    def save(self):
        MEMORY_FILE.write_text(json.dumps(self.memory, indent=2))

    def load(self):
        if MEMORY_FILE.exists():
            self.memory = json.loads(MEMORY_FILE.read_text())


MEMORY = DistributedMemory()