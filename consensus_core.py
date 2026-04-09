# consensus_core.py

import random


class ConsensusCore:

    def __init__(self, grid, energy_model):
        self.grid = grid
        self.energy = energy_model

    def collect_votes(self, proposal):

        votes = []

        for name, box in self.grid.boxes.items():

            energy = self.energy.nodes[name].energy

            vote_strength = energy / 2000

            decision = random.random() < vote_strength

            votes.append(1 if decision else 0)

        return votes

    def decide(self, proposal):

        votes = self.collect_votes(proposal)

        agreement = sum(votes) / len(votes)

        print(f"[Consensus] agreement={agreement:.2f}")

        return agreement > 0.6