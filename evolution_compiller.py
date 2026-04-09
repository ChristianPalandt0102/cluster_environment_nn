# evolution_compiler.py

import importlib
import json
import time

class EvolutionCompiler:

    def __init__(self, dream_engine):
        self.dream_engine = dream_engine
        self.history = []

    def evaluate_dreams(self):
        dreams = self.dream_engine.generate_predictions()

        compiled = []
        for d in dreams:
            if self.score(d) > 0.65:
                compiled.append(d)

        return compiled

    def score(self, dream):
        complexity = dream.get("complexity", 0.5)
        stability = dream.get("stability", 0.5)
        return (complexity + stability) / 2

    def deploy(self, compiled):
        for module in compiled:
            print(f"[Evolution] deploying {module['name']}")
            self.history.append(module)

    def cycle(self):
        compiled = self.evaluate_dreams()
        self.deploy(compiled)