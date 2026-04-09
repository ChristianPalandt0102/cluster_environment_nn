# neuro_symbolic_cortex.py

class NeuroSymbolicCortex:

    def __init__(self):
        self.rules = {
            "high_load": "reroute",
            "low_load": "compress",
            "unstable": "stabilize"
        }

    def interpret(self, nn_score):

        if nn_score > 0.75:
            return self.rules["high_load"]
        elif nn_score < 0.3:
            return self.rules["low_load"]
        return self.rules["unstable"]

    def combine(self, neural_output):
        action = self.interpret(neural_output)
        return {
            "decision": action,
            "confidence": neural_output
        }