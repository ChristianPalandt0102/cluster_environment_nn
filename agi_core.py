# agi_core.py

from curiosity_engine import CuriosityEngine
from discovery_engine import DiscoveryEngine
from neuro_symbolic_cortex import NeuroSymbolicCortex
from memory_consciousness import MEMORY


class AGICore:

    def __init__(self):
        self.curiosity = CuriosityEngine()
        self.discovery = DiscoveryEngine()
        self.reasoning = NeuroSymbolicCortex()

    def think(self):

        curiosity_event = self.curiosity.decide_exploration()

        hypothesis = self.discovery.formulate_hypothesis(
            curiosity_event["question"]
        )

        decision = self.reasoning.combine(
            curiosity_event["score"]
        )

        MEMORY.learn("last_decision", decision)

        return {
            "curiosity": curiosity_event,
            "hypothesis": hypothesis,
            "decision": decision
        }