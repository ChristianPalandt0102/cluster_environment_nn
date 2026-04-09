# neural_traffic_cortex.py

import random

class NeuralTrafficCortex:

    def __init__(self, nodes):
        self.nodes = nodes
        self.neurons = {
            (a, b): random.random()
            for a in nodes for b in nodes if a != b
        }

    def reinforce(self, a, b, success):
        delta = 0.05 if success else -0.03
        self.neurons[(a, b)] += delta

    def choose(self, current):
        options = [
            (n, self.neurons[(current, n)])
            for n in self.nodes if n != current
        ]

        options.sort(key=lambda x: -x[1])
        return options[0][0]