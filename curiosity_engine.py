# curiosity_engine.py

import random

# curiosity_engine.py

import random
from code_discovery_engine import DISCOVERY_ENGINE


class CuriosityEngine:

    def __init__(self):
        self.curiosity_level = 0.5

    def evaluate(self):
        self.curiosity_level += random.uniform(-0.1, 0.2)
        self.curiosity_level = max(0, min(1, self.curiosity_level))

    def generate_goal(self):
        goals = [
            "optimize_network",
            "invent_signal",
            "mutate_algorithm",
            "explore_topology"
        ]
        return random.choice(goals)

    def run(self):
        self.evaluate()

        if self.curiosity_level > 0.6:
            goal = self.generate_goal()
            print("[CURIOSITY]", goal)
            DISCOVERY_ENGINE.evolve_cycle()


CURIOSITY = CuriosityEngine()




class CuriosityEngine:

    QUESTIONS = [
        "Can latency be predicted earlier?",
        "Should routing topology mutate?",
        "Is cache hierarchy optimal?",
        "Can GAN invent better scheduling?",
        "Should new sandbox species emerge?"
    ]

    def generate_question(self):
        return random.choice(self.QUESTIONS)

    def curiosity_score(self):
        return random.random()

    def decide_exploration(self):
        score = self.curiosity_score()
        return {
            "explore": score > 0.4,
            "score": score,
            "question": self.generate_question()
        }