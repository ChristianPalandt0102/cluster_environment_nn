# stream_safety.py

class StreamSafety:

    def __init__(self):
        self.max_rate = 50  # msgs per cycle

    def filter(self, messages):

        safe = []

        for m in messages[:self.max_rate]:

            if "data" in m:
                safe.append(m)

        return safe