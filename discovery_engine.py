# discovery_engine.py

import random

class DiscoveryEngine:

    def __init__(self):
        self.knowledge_base = []

    def formulate_hypothesis(self, question):
        return {
            "question": question,
            "hypothesis": f"Adjust parameter {random.randint(1,5)}"
        }

    def experiment(self, physics_engine):
        result = physics_engine.evaluate_system(
            random.uniform(0.2, 1.0)
        )
        return result

    def evaluate(self, experiment_result):
        success = experiment_result["throughput"] > \
                  experiment_result["latency"]
        return success

    def learn(self, hypothesis, success):
        record = {
            "hypothesis": hypothesis,
            "success": success
        }
        self.knowledge_base.append(record)
        return record