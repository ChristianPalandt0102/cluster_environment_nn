# future_simulation.py

import random
from memory_cortex import MEMORY


class FutureSimulation:

    def simulate(self, intent, variants=5):
        futures = []

        for i in range(variants):
            score = random.uniform(0, 1)

            futures.append({
                "intent": intent,
                "score": score,
                "timeline": i
            })

        return sorted(futures, key=lambda x: x["score"], reverse=True)

    def choose(self, intent):
        futures = self.simulate(intent)
        best = futures[0]

        MEMORY.remember_event(
            f"future_selected:{best}"
        )

        return best


FUTURE_SIM = FutureSimulation()