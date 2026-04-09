
# L5_cache.py

from collections import deque
import json
import os

MB = 1024 * 1024


# ----------------------------------------
# CACHE STAGE
# ----------------------------------------
class CacheStage:

    def __init__(self, name, limit_mb):
        self.name = name
        self.limit = limit_mb * MB
        self.buffer = deque()
        self.size = 0

    # -------------------------
    def push(self, item):

        data = json.dumps(item)
        size = len(data.encode())

        if self.size + size > self.limit:
            return False

        self.buffer.append(data)
        self.size += size
        return True

    # -------------------------
    def pop(self):

        if not self.buffer:
            return None

        data = self.buffer.popleft()
        self.size -= len(data.encode())
        return json.loads(data)


# ----------------------------------------
# CACHE LEVEL (2-stage)
# ----------------------------------------
class CacheLevel:

    def __init__(self, name, stageA_mb, stageB_mb):
        self.name = name
        self.A = CacheStage(f"{name}-A", stageA_mb)
        self.B = CacheStage(f"{name}-B", stageB_mb)

    def push(self, item):

        # try hot cache
        if self.A.push(item):
            return "A"

        # overflow into shadow cache
        if self.B.push(item):
            return "B"

        return None

    def pop(self):
        item = self.A.pop()
        if item:
            return item
        return self.B.pop()


# ----------------------------------------
# GLOBAL CACHE SYSTEM
# ----------------------------------------
class L5CacheSystem:

    def __init__(self):

        self.levels = [
            CacheLevel("L1", 24, 24),
            CacheLevel("L2", 64, 64),
            CacheLevel("L3", 128, 128),
            CacheLevel("L4", 1024, 256),
            CacheLevel("L5", 256, 256),
        ]

        self.spill_file = "overflow_spill.json"

    # --------------------------------
    def store(self, item):

        for level in self.levels:
            stage = level.push(item)

            if stage:
                return f"{level.name}-{stage}"

        # FINAL SAFETY → disk spill
        self._spill_to_disk(item)
        return "DISK"

    # --------------------------------
    def retrieve(self):

        for level in self.levels:
            item = level.pop()
            if item:
                return item

        return self._load_spill()

    # --------------------------------
    def _spill_to_disk(self, item):

        data = []
        if os.path.exists(self.spill_file):
            with open(self.spill_file) as f:
                data = json.load(f)

        data.append(item)

        with open(self.spill_file, "w") as f:
            json.dump(data, f)

    # --------------------------------
    def _load_spill(self):

        if not os.path.exists(self.spill_file):
            return None

        with open(self.spill_file) as f:
            data = json.load(f)

        if not data:
            return None

        item = data.pop(0)

        with open(self.spill_file, "w") as f:
            json.dump(data, f)

        return item

def prefetch(self, predicted_items):
    for item in predicted_items:
        self.store(item)