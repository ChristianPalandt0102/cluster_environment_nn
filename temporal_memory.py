# temporal_memory.py

import json
import time
import os


class TemporalMemory:

    FILE = "timeline_memory.json"

    def __init__(self):
        self.timeline = self._load()

    # ------------------------------
    def remember(self, state, result):

        entry = {
            "time": time.time(),
            "state": state,
            "result": result
        }

        self.timeline.append(entry)
        self._save()

    # ------------------------------
    def recall_similar(self, state):

        if not self.timeline:
            return None

        # simple similarity search
        return min(
            self.timeline,
            key=lambda e: abs(
                e["state"].get("cache_pressure", 0)
                - state.get("cache_pressure", 0)
            )
        )

    # ------------------------------
    def _load(self):
        if os.path.exists(self.FILE):
            return json.load(open(self.FILE))
        return []

    def _save(self):
        json.dump(self.timeline, open(self.FILE, "w"))