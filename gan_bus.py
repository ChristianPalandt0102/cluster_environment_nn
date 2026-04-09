# gan_bus.py

import numpy as np


class Generator:
    def generate(self):
        return np.random.rand(8, 8)


class Discriminator:

    def evaluate(self, sample):
        score = np.mean(sample)
        return 1 if score > 0.5 else 0


class GANBus:

    def __init__(self):
        self.G = Generator()
        self.D = Discriminator()

    def train_step(self):
        fake = self.G.generate()
        result = self.D.evaluate(fake)

        return {
            "generated_mean": float(np.mean(fake)),
            "accepted": bool(result)
        }