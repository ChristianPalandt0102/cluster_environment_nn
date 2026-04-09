# reality_simulation.py

import random

class RealitySimulation:

    def __init__(self):
        self.worlds = []

    def simulate_world(self):
        return {
            "latency": random.uniform(0.1, 1.0),
            "stability": random.uniform(0.1, 1.0),
            "throughput": random.uniform(0.1, 1.0)
        }

    def run(self, iterations=5):
        self.worlds = [self.simulate_world() for _ in range(iterations)]
        return self.worlds

    def best_future(self):
        return max(
            self.worlds,
            key=lambda w: w["stability"] + w["throughput"]
        )