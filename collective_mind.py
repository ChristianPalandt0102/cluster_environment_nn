# collective_mind.py

import time
from collections import defaultdict


class CollectiveMind:

    def __init__(self):
        self.node_states = {}
        self.shared_thoughts = defaultdict(list)

    # nodes publish awareness
    def publish(self, node, thought, value):
        self.node_states[node] = time.time()
        self.shared_thoughts[thought].append(value)

    # consensus calculation
    def consensus(self, thought):
        values = self.shared_thoughts.get(thought, [])

        if not values:
            return None

        return sum(values) / len(values)

    # global awareness
    def global_state(self):
        return {
            "nodes": len(self.node_states),
            "thoughts": len(self.shared_thoughts)
        }


COLLECTIVE = CollectiveMind()