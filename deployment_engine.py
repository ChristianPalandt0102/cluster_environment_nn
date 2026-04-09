# deployment_engine.py

import random
from self_model import SELF_MODEL


class DeploymentEngine:

    def __init__(self):
        self.counter = 0

    def analyze(self):
        model = SELF_MODEL.snapshot()

        overloaded = [
            b for b, data in model["boxes"].items()
            if len(data["ports"]) > 8
        ]

        return overloaded

    def deploy_box(self):
        self.counter += 1
        name = f"AUTO_{self.counter}"

        ports = list(range(
            7000 + self.counter*10,
            7000 + self.counter*10 + 10
        ))

        SELF_MODEL.register_box(name, ports)

        print(f"[DEPLOY] new sandbox {name}")

    def run_cycle(self):
        overloaded = self.analyze()

        if overloaded:
            self.deploy_box()


DEPLOYMENT_ENGINE = DeploymentEngine()