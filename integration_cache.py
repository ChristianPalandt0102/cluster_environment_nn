# integration_cache.py

import numpy as np

MB = 1024 * 1024


class IntegrationArrayCache:
    """
    8-bit compressed state cache
    """

    def __init__(self, size_mb=16):

        entries = size_mb * MB
        self.cache = np.zeros(entries, dtype=np.uint8)

    def set_state(self, idx, state):
        self.cache[idx % len(self.cache)] = state & 0xFF

    def get_state(self, idx):
        return int(self.cache[idx % len(self.cache)])

    def entropy(self):
        return float(self.cache.std())