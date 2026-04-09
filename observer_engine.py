from gpu_buffer import GPUScoreBuffer
from integration_cache import IntegrationArrayCache


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