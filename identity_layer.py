# identity_layer.py

import uuid
import random

class Identity:

    TRAITS = [
        "explorer",
        "optimizer",
        "stabilizer",
        "inventor",
        "analyst"
    ]

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.trait = random.choice(self.TRAITS)
        self.memory = []

    def remember(self, event):
        self.memory.append(event)
        self.memory = self.memory[-50:]  # bounded memory

    def personality_bias(self):
        return {
            "explorer": 1.2,
            "optimizer": 1.1,
            "stabilizer": 0.9,
            "inventor": 1.3,
            "analyst": 1.0
        }[self.trait]