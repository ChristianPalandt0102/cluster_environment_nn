from future_simulation import FUTURE_SIM

from deployment_engine import DEPLOYMENT_ENGINE

def autonomous_intent(self):
    DEPLOYMENT_ENGINE.run_cycle()
    self.intent_queue.append(("self_expand", {}))


best = FUTURE_SIM.choose(name)
FACTORY.submit(best["intent"], payload)