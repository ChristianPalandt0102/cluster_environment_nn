# neural_bus_controller.py

import numpy as np
from nn_bus import NNBus
from gan_bus import GANBus
from organizer import BusOrganizer


class NeuralBusController:

    def __init__(self):
        self.nn = NNBus()
        self.gan = GANBus()
        self.organizer = BusOrganizer()

    def cycle(self):

        # simulate system signal
        signal = np.random.rand(12, 12)

        encoded, score = self.nn.process(signal)

        gan_result = self.gan.train_step()

        decision = self.organizer.evaluate(score, gan_result)

        return {
            "nn_score": score,
            "gan": gan_result,
            "decision": decision
        }