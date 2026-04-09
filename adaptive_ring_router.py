# adaptive_ring_router.py

import random

class AdaptiveRingRouter:

    def __init__(self, nodes):
        self.nodes = nodes
        self.weights = {
            (a, b): 1.0
            for a in nodes
            for b in nodes if a != b
        }

    def record_latency(self, a, b, latency):
        self.weights[(a, b)] *= (1 + latency * 0.01)

    def choose_next(self, current):
        options = [
            (n, self.weights[(current, n)])
            for n in self.nodes if n != current
        ]

        options.sort(key=lambda x: x[1])
        return options[0][0]

    def route(self, start, hops=5):
        path = [start]
        current = start

        for _ in range(hops):
            current = self.choose_next(current)
            path.append(current)

        return path