# anomaly_engine.py

import statistics


class AnomalyEngine:

    def __init__(self):
        self.history = []

    def detect(self, fusion):

        score = fusion["fusion_score"]

        self.history.append(score)
        self.history = self.history[-50:]  # sliding window

        if len(self.history) < 5:
            return {"anomaly": False}

        mean = statistics.mean(self.history)
        stdev = statistics.stdev(self.history)

        # anomaly condition
        if abs(score - mean) > 2 * stdev:
            return {
                "anomaly": True,
                "type": "spike",
                "score": score,
                "mean": mean
            }

        # entropy anomaly
        if score > 3.0:
            return {
                "anomaly": True,
                "type": "high_intensity",
                "score": score
            }

        return {"anomaly": False}