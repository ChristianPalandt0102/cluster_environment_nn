# evolution_engine.py

import random
from factory_bus import FACTORY


class WorkerDNA:

    def __init__(self):
        self.sleep_factor = 0.01
        self.parallel_bias = 1.0


class EvolutionEngine:

    def __init__(self):
        self.population = {}

    def evolve(self):
        bench = FACTORY.benchmark()

        for wid, data in bench.items():
            dna = self.population.setdefault(wid, WorkerDNA())

            # mutation rule
            if data["avg_time"] > 0.02:
                dna.sleep_factor *= random.uniform(0.8, 0.95)
            else:
                dna.sleep_factor *= random.uniform(1.01, 1.1)

            print(f"[EVOLVE] {wid} sleep={dna.sleep_factor:.4f}")


EVOLUTION_ENGINE = EvolutionEngine()