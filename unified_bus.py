# unified_bus.py

from factory_bus import FactoryBus
from nn_bus import NNBus
from quantum_bus import QuantumBus
from system_output.exporter import SystemExporter


class UnifiedBus:

    def __init__(self):

        self.factory = FactoryBus()
        self.nn = NNBus()
        self.quantum = QuantumBus()
        self.exporter = SystemExporter()

    # --- CORE CYCLE ---

    def cycle(self):

        # 1. Gather system state
        q_state = self.quantum.sample_state()

        # 2. Neural evaluation
        nn_result = self.nn.process(q_state)

        # 3. Decide workload
        tasks = self.factory.plan(nn_result)

        # 4. Execute tasks
        results = self.factory.execute(tasks)

        # 5. Feedback loop
        self.nn.learn(results)
        self.quantum.update(results)

        # 6. Export state
        data = {
            "quantum": q_state,
            "nn": nn_result,
            "tasks": tasks,
            "results": results
        }

        self.exporter.stream(data)

        return data