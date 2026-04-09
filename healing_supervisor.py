# healing_supervisor.py

import time
import threading
from factory_bus import FACTORY


class HealingSupervisor(threading.Thread):

    def __init__(self, check_interval=5):
        super().__init__(daemon=True)
        self.interval = check_interval

    def run(self):
        while True:
            self.inspect_workers()
            time.sleep(self.interval)

    def inspect_workers(self):
        alive = [w for w in FACTORY.workers if w.is_alive()]
        missing = len(FACTORY.workers) - len(alive)

        if missing > 0:
            print(f"[HEAL] rebuilding {missing} workers")
            FACTORY.spawn_workers(missing)


HEALING_SUPERVISOR = HealingSupervisor()