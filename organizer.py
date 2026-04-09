# organizer.py

import random


class BusOrganizer:

    def __init__(self):
        self.state = {
            "mode": "observe",
            "fitness": 0.5
        }

    def evaluate(self, nn_score, gan_result):

        fitness = (nn_score + gan_result["generated_mean"]) / 2
        self.state["fitness"] = fitness

        if fitness > 0.7:
            self.state["mode"] = "expand"
        elif fitness < 0.3:
            self.state["mode"] = "mutate"
        else:
            self.state["mode"] = "stabilize"

        return self.state