# fusion_engine.py

class FusionEngine:

    def __init__(self):
        self.weights = {
            "finance": 1.0,
            "news": 0.8,
            "weather": 0.6
        }

    def normalize(self, stream):

        normalized = []

        for msg in stream:

            source = msg["source"]

            if "btc" in source:
                domain = "finance"
            elif "news" in source:
                domain = "news"
            elif "weather" in source:
                domain = "weather"
            else:
                domain = "unknown"

            normalized.append({
                "domain": domain,
                "data": msg["data"]
            })

        return normalized

    def fuse(self, stream):

        normalized = self.normalize(stream)

        score = 0
        signals = []

        for item in normalized:

            weight = self.weights.get(item["domain"], 0.5)

            # simple scoring (extend later)
            signals.append({
                "domain": item["domain"],
                "weight": weight
            })

            score += weight

        return {
            "fusion_score": score,
            "signals": signals
        }