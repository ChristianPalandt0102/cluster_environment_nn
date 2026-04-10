# controller_engine.py

import random


class ControllerEngine:

    def __init__(self):
        self.modes = [
            "stabilize",
            "amplify",
            "isolate",
            "evolve",
            "observe"
        ]

    def decide(self, anomaly, nn_result):

        if not anomaly.get("anomaly"):
            return {"action": "observe"}

        t = anomaly.get("type")

        if t == "spike":
            return {"action": "stabilize"}

        if t == "high_intensity":
            return {"action": "isolate"}

        # fallback
        return {"action": random.choice(self.modes)}

    def apply(self, action, system):

        if action == "stabilize":
            system.factory.throttle = True

        elif action == "amplify":
            system.nn.boost = True

        elif action == "isolate":
            system.network_blocked = True

        elif action == "evolve":
            system.force_evolution = True

        return {"applied": action}