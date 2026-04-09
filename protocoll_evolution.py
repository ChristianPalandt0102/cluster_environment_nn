# protocol_evolution.py

class ProtocolEvolution:

    def __init__(self):
        self.usage_stats = {}

    def record(self, symbol):
        self.usage_stats[symbol] = self.usage_stats.get(symbol, 0) + 1

    def optimize(self, upl):

        # frequently used → shorter encoding
        sorted_usage = sorted(
            self.usage_stats.items(),
            key=lambda x: -x[1]
        )

        for i, (symbol, _) in enumerate(sorted_usage[:5]):
            upl.dictionary[f"S{i}"] = upl.dictionary[symbol]