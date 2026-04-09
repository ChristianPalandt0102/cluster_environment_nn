# identity_core.py

import json
import uuid
from pathlib import Path

IDENTITY_FILE = Path("identity.json")


class IdentityCore:

    def __init__(self):
        self.identity = {
            "id": str(uuid.uuid4()),
            "name": "ClusterMind",
            "traits": {
                "curiosity": 0.7,
                "stability": 0.5,
                "exploration": 0.6
            },
            "evolution_stage": 1,
            "behavior_bias": "adaptive"
        }
        self.load()

    def evolve(self):
        self.identity["evolution_stage"] += 1
        self.save()

    def adjust_trait(self, trait, delta):
        self.identity["traits"][trait] += delta
        self.identity["traits"][trait] = max(
            0, min(1, self.identity["traits"][trait])
        )
        self.save()

    def save(self):
        IDENTITY_FILE.write_text(
            json.dumps(self.identity, indent=2)
        )

    def load(self):
        if IDENTITY_FILE.exists():
            self.identity = json.loads(
                IDENTITY_FILE.read_text()
            )


IDENTITY = IdentityCore()