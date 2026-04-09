# kernel_scheduler.py

import time
import random


class KernelScheduler:

    def __init__(self, grid, cache):
        self.grid = grid
        self.cache = cache
        self.metrics = {}

    # --------------------------------
    def observe(self):

        pressure = [
            lvl.A.size + lvl.B.size
            for lvl in self.cache.levels
        ]

        self.metrics = {
            "cache_pressure": sum(pressure),
            "timestamp": time.time()
        }

        return self.metrics

    # --------------------------------
    def optimize(self):

        for box in self.grid.boxes.values():

            # dynamic priority mutation
            box.priority = random.uniform(0.5, 1.5)

        print("[Kernel] priorities rebalanced")

    # --------------------------------
    def cycle(self):

        self.observe()

        if self.metrics["cache_pressure"] > 50_000_000:
            self.optimize()