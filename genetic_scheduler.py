# genetic_scheduler.py
import random


class GeneticScheduler:

    def select_box(self, task, boxes):

        scores = []

        for box in boxes:
            fitness = (
                task["dna"]["survival_score"]
                * random.uniform(0.8, 1.2)
            )

            scores.append((fitness, box))

        scores.sort(reverse=True)

        return scores[0][1]

    def evolve(self, task):

        task["dna"]["mutation_rate"] *= random.uniform(0.95, 1.05)
        task["dna"]["survival_score"] *= random.uniform(0.9, 1.1)

        return task