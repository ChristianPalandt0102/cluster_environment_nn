# software_civilization.py

import random
import time

class SoftwareAgent:

    def __init__(self, name):
        self.name = name
        self.skills = []
        self.energy = random.random()

    def develop_skill(self):
        skill = random.choice([
            "optimizer",
            "router",
            "predictor",
            "compressor",
            "simulator"
        ])
        self.skills.append(skill)
        return skill

    def mutate(self):
        if self.skills:
            self.skills[random.randint(0, len(self.skills)-1)] += "_v2"

    def state(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "energy": self.energy
        }


class SoftwareCivilization:

    def __init__(self, boxes):
        self.agents = [SoftwareAgent(b) for b in boxes]

    def evolve_cycle(self):
        for agent in self.agents:
            if random.random() > 0.5:
                agent.develop_skill()
            else:
                agent.mutate()

        return [a.state() for a in self.agents]