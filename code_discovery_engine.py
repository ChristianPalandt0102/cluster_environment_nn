# code_discovery_engine.py

import random
import types
from factory_bus import FACTORY


class CodeGenome:

    def __init__(self, source):
        self.source = source
        self.score = 0


class CodeDiscoveryEngine:

    def __init__(self):
        self.genomes = []

    # ---- generate mutation ----
    def mutate(self, base_code: str):
        mutations = [
            "x+1",
            "x*2",
            "x**2",
            "x-1"
        ]
        expr = random.choice(mutations)

        code = f"""
def evolved_function(x):
    return {expr}
"""
        return CodeGenome(code)

    # ---- sandbox test ----
    def test(self, genome):
        namespace = {}
        exec(genome.source, namespace)

        fn = namespace["evolved_function"]

        score = sum(fn(i) for i in range(5))
        genome.score = score
        self.genomes.append(genome)

    def evolve_cycle(self):
        base = "def f(x): return x"
        genome = self.mutate(base)
        self.test(genome)

        print("[DISCOVERY] new genome score:", genome.score)


DISCOVERY_ENGINE = CodeDiscoveryEngine()