# gpu_buffer.py

import numpy as np

MB = 1024 * 1024


class GPUScoreBuffer:
    """
    32-bit floating score buffer
    """

    def __init__(self, size_mb=16):

        entries = (size_mb * MB) // 4
        self.buffer = np.zeros(entries, dtype=np.float32)

    def write(self, idx, value):
        self.buffer[idx % len(self.buffer)] = value

    def read(self, idx):
        return float(self.buffer[idx % len(self.buffer)])

    def accumulate(self, idx, value):
        self.buffer[idx % len(self.buffer)] += value

    def global_score(self):
        return float(self.buffer.mean())