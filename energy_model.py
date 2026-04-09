# energy_model.py

import time
import random


class EnergyNode:

    def __init__(self, name):
        self.name = name
        self.energy = 1000.0
        self.last_update = time.time()

    def recharge(self):
        dt = time.time() - self.last_update
        self.energy += dt * 5
        self.energy = min(self.energy, 2000)
        self.last_update = time.time()

    def consume(self, amount):
        self.recharge()
        if self.energy >= amount:
            self.energy -= amount
            return True
        return False


class EnergyModel:

    def __init__(self, grid):
        self.nodes = {
            name: EnergyNode(name)
            for name in grid.boxes
        }

    def request_execution(self, box, cost):

        node = self.nodes[box]

        if node.consume(cost):
            return True

        print(f"[Energy] denied execution at {box}")
        return False

    def global_state(self):
        return {
            n: node.energy for n, node in self.nodes.items()
        }