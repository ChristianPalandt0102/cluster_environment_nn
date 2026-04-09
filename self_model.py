# self_model.py

import json
from pathlib import Path

MODEL_FILE = Path("self_model.json")


class SelfModel:

    def __init__(self):
        self.state = {
            "boxes": {},
            "ports": {},
            "workers": {},
            "health": {}
        }
        self.load()

    # ---- register components ----
    def register_box(self, name, ports):
        self.state["boxes"][name] = {
            "ports": ports,
            "status": "active"
        }
        self.save()

    def register_worker(self, wid, box):
        self.state["workers"][wid] = {
            "box": box,
            "load": 0
        }

    def update_health(self, component, value):
        self.state["health"][component] = value
        self.save()

    # ---- introspection ----
    def snapshot(self):
        return self.state

    def save(self):
        MODEL_FILE.write_text(json.dumps(self.state, indent=2))

    def load(self):
        if MODEL_FILE.exists():
            self.state = json.loads(MODEL_FILE.read_text())


SELF_MODEL = SelfModel()