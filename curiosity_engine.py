# curiosity_engine.py

import random

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