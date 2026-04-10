import statistics

class AnomalyEngine:

    def __init__(self):
        self.history = []

    def detect(self, fusion):

        score = fusion["fusion_score"]
        self.history.append(score)
        self.history = self.history[-20:]

        if len(self.history) < 5:
            return {"anomaly": False}

        mean = statistics.mean(self.history)

        if score > mean * 1.5:
            return {"anomaly": True, "type": "spike"}

        return {"anomaly": False}