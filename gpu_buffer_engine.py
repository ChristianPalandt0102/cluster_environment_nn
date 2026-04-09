# gpu_buffer_engine.py
import array
import threading
import random
import time

class GPUBuffer32:
    """
    Simulated 32-bit GPU scoring buffer
    """

    def __init__(self, size_mb=32):
        self.size = size_mb * 1024 * 1024 // 4   # 4 bytes per float
        self.buffer = array.array("f", [0.0] * self.size)
        self.lock = threading.Lock()

    def write(self, index, value):
        with self.lock:
            self.buffer[index % self.size] = float(value)

    def read(self, index):
        with self.lock:
            return self.buffer[index % self.size]

    def score_activity(self):
        """
        Calculate system activity score
        """
        with self.lock:
            sample = self.buffer[:1000]
            return sum(sample) / (len(sample) or 1)

    def randomize(self):
        with self.lock:
            for i in range(1000):
                self.buffer[random.randint(0, self.size-1)] = random.random()