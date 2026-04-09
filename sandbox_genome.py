# sandbox_genome.py

import random

class SandboxGenome:

    def __init__(self, name):
        self.name = name
        self.dna = {
            "compute_bias": random.random(),
            "network_bias": random.random(),
            "mutation_rate": 0.05,
            "stability": 1.0
        }

    def mutate(self):
        for key in self.dna:
            if random.random() < self.dna["mutation_rate"]:
                self.dna[key] += random.uniform(-0.1, 0.1)

    def fitness(self, metrics):
        score = (
            metrics["throughput"] * self.dna["compute_bias"]
            - metrics["latency"] * self.dna["network_bias"]
        )
        self.dna["stability"] = max(0, score)
        return score