# quantum_prediction_engine.py

import random

class QuantumPredictor:

    def __init__(self):
        self.history = []

    def observe(self, signal):
        self.history.append(signal)

    def predict_load(self):
        if not self.history:
            return 0.5

        return sum(self.history[-10:]) / min(len(self.history), 10)

    def predict_route_shift(self):
        load = self.predict_load()

        if load > 0.7:
            return "reroute"
        elif load < 0.3:
            return "compress"
        return "stable"