# memory_cortex.py

import json
import time
from pathlib import Path
import threading

CORTEX_DB = "cortex_memory.json"


class MemoryCortex:

    def __init__(self):
        self.lock = threading.Lock()
        self.memory = self._load()

    def _load(self):
        try:
            with open(CORTEX_DB) as f:
                return json.load(f)
        except:
            return {"events": []}

    def remember(self, source, event):

        with self.lock:
            self.memory["events"].append({
                "source": source,
                "event": event
            })
            self._save()

    def query(self, key):
        return [e for e in self.memory["events"] if key in str(e)]

    def _save(self):
        with open(CORTEX_DB, "w") as f:
            json.dump(self.memory, f, indent=2)



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