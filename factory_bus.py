import time
import uuid
import threading
from queue import Queue
from dataclasses import dataclass, field
from typing import Callable, Dict, List

from bus.config import SYSTEM_BUS
from quantum_bus.config import QUANTUM_BUS

from neural_bus_controller import NeuralBusController
from evolution_engine import EVOLUTION_ENGINE
from factory_master import FactoryMaster
from bus.config import BUS_CONFIG


# factory_bus.py



# =========================
# TASK MODEL
# =========================

@dataclass
class Task:
    id: str
    name: str
    payload: dict
    created: float = field(default_factory=time.time)


# =========================
# WORKER
# =========================

class Worker(threading.Thread):

    def __init__(self, wid: str, queue: Queue, bench):
        super().__init__(daemon=True)
        self.wid = wid
        self.queue = queue
        self.bench = bench
        self.running = True

    def run(self):
        while self.running:
            task = self.queue.get()

            start = time.time()
            try:
                self.execute(task)
            finally:
                duration = time.time() - start
                self.bench.record(self.wid, duration)

    def execute(self, task: Task):
        print(f"[Worker {self.wid}] executing {task.name}")
        time.sleep(0.01)  # simulated workload


# =========================
# BENCHMARK ENGINE
# =========================

class BenchSystem:

    def __init__(self):
        self.metrics: Dict[str, List[float]] = {}

    def record(self, worker_id, duration):
        self.metrics.setdefault(worker_id, []).append(duration)

    def summary(self):
        result = {}
        for w, times in self.metrics.items():
            result[w] = {
                "runs": len(times),
                "avg_time": sum(times) / len(times)
            }
        return result


# =========================
# MASTER FACTORY
# =========================

class MasterFactory:

    def __init__(self):
        self.queue = Queue()
        self.bench = BenchSystem()
        self.workers: List[Worker] = []

    # ---- worker creation ----
    def spawn_workers(self, count=4):
        for _ in range(count):
            wid = str(uuid.uuid4())[:8]
            w = Worker(wid, self.queue, self.bench)
            w.start()
            self.workers.append(w)

    # ---- workload flow ----
    def submit(self, name, payload):
        task = Task(
            id=str(uuid.uuid4()),
            name=name,
            payload=payload
        )
        self.queue.put(task)

    # ---- benchmark output ----
    def benchmark(self):
        return self.bench.summary()


# global factory
FACTORY = MasterFactory()



def execute(self, task):
    dna = EVOLUTION_ENGINE.population.get(self.wid)
    delay = dna.sleep_factor if dna else 0.01

    time.sleep(delay)


NN_CONTROLLER = NeuralBusController()

def neural_cycle():
    result = NN_CONTROLLER.cycle()
    print("[NN BUS]", result)

# factory_bus.py

class FactoryBus:

    def __init__(self):
        self.master = FactoryMaster(
            BUS_CONFIG["allowed_ports"][:30]
        )

    def boot(self):
        print("FactoryBus booting...")
        self.master.start_cluster()

    def benchmark(self):
        return {
            "workers": len(self.master.workers),
            "status": "running"
        }