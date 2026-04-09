# research_agent.py

import random
import asyncio


class ResearchAgent:

    def __init__(self, operation_boxes, temporal_memory):
        self.ops = operation_boxes
        self.memory = temporal_memory

    # --------------------------------
    def generate_experiment(self):

        return {
            "mutation": random.choice([
                "routing_shift",
                "cache_resize",
                "signal_compression",
                "scheduler_bias"
            ]),
            "intensity": random.random()
        }

    # --------------------------------
    async def run_experiment(self):

        experiment = self.generate_experiment()

        snapshot = self.ops.collect_snapshot()

        futures = self.ops.simulate_routes(snapshot)

        best = self.ops.evaluate(futures)

        self.memory.remember(snapshot, {
            "experiment": experiment,
            "score": best.score
        })

        print("[Research] experiment stored")