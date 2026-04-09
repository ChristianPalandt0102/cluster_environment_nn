from gpu_buffer import GPUScoreBuffer
from integration_cache import IntegrationArrayCache

class ConsciousnessMeter:

    def __init__(self):
        self.signals = 0
        self.mutations = 0
        self.routing_changes = 0

    def event(self, kind):

        if kind == "signal":
            self.signals += 1
        elif kind == "mutation":
            self.mutations += 1
        elif kind == "rewire":
            self.routing_changes += 1

    def score(self):

        return (
            self.signals*0.3 +
            self.mutations*2 +
            self.routing_changes*3
        )



class ConsciousnessGPU:

    def __init__(self):

        self.gpu = GPUScoreBuffer(16)
        self.cache = IntegrationArrayCache(16)

        self.pointer = 0

    def signal_event(self, strength):

        self.gpu.accumulate(self.pointer, strength)

        # compress into 8-bit state
        state = int(min(strength * 25, 255))
        self.cache.set_state(self.pointer, state)

        self.pointer += 1

    def score(self):

        base = self.gpu.global_score()
        entropy = self.cache.entropy()

        return base + entropy * 0.1