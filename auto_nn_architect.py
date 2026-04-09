# auto_nn_architect.py

import random

class AutoNNArchitect:

    def __init__(self):
        self.archives = []

    def propose_architecture(self):
        return {
            "layers": random.randint(2, 6),
            "kernel": random.choice([3,5]),
            "channels": random.choice([8,16,32]),
            "activation": random.choice(["tanh","relu"])
        }

    def evaluate(self, score):
        return score > 0.6

    def evolve(self, nn_score):
        arch = self.propose_architecture()

        if self.evaluate(nn_score):
            self.archives.append(arch)

        return arch