# memory_cortex.py

import json
import time
from pathlib import Path


MEMORY_FILE = Path("memory_cortex.json")


class MemoryCortex:

    def __init__(self):
        self.memory = {
            "episodes": [],
            "knowledge": {},
            "skills": {}
        }
        self.load()

    def remember_event(self, event):
        self.memory["episodes"].append({
            "time": time.time(),
            "event": event
        })
        self.save()

    def learn(self, key, value):
        self.memory["knowledge"][key] = value
        self.save()

    def skill(self, name, data):
        self.memory["skills"][name] = data
        self.save()

    def save(self):
        MEMORY_FILE.write_text(json.dumps(self.memory, indent=2))

    def load(self):
        if MEMORY_FILE.exists():
            self.memory = json.loads(MEMORY_FILE.read_text())


MEMORY = MemoryCortex()