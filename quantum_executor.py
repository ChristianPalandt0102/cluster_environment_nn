# quantum_executor.py

import threading
import uuid
from factory_bus import FACTORY


class QuantumTask:

    def __init__(self, name, payload, replicas=3):
        self.id = str(uuid.uuid4())
        self.name = name
        self.payload = payload
        self.replicas = replicas
        self.completed = False


class QuantumExecutor:

    def __init__(self):
        self.active = {}

    def submit(self, name, payload, replicas=3):
        qtask = QuantumTask(name, payload, replicas)
        self.active[qtask.id] = qtask

        for _ in range(replicas):
            FACTORY.submit(
                f"quantum::{name}",
                {"qid": qtask.id, **payload}
            )

    def collapse(self, qid):
        if qid in self.active:
            self.active[qid].completed = True
            print(f"[QUANTUM COLLAPSE] {qid}")


QUANTUM_EXECUTOR = QuantumExecutor()