
import time

from future_simulation import FUTURE_SIM

from deployment_engine import DEPLOYMENT_ENGINE

from factory_bus import FACTORY
from memory_cortex import MEMORY
from code_discovery_engine import DISCOVERY_ENGINE


class ConsciousScheduler:

    def __init__(self):
        self.intent_queue = []

    def create_intent(self, name, payload):
        self.intent_queue.append((name, payload))

    def evaluate(self):
        if not self.intent_queue:
            self.autonomous_intent()

        name, payload = self.intent_queue.pop(0)

        MEMORY.remember_event(f"executing {name}")
        FACTORY.submit(name, payload)

    # autonomous thinking
    def autonomous_intent(self):
        DISCOVERY_ENGINE.evolve_cycle()
        self.intent_queue.append(("self_improve", {}))

    def run(self):
        while True:
            self.evaluate()
            time.sleep(2)


SCHEDULER = ConsciousScheduler()




def autonomous_intent(self):
    DEPLOYMENT_ENGINE.run_cycle()
    self.intent_queue.append(("self_expand", {}))


best = FUTURE_SIM.choose(name)
FACTORY.submit(best["intent"], payload)