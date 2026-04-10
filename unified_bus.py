# unified_bus.py

from factory_bus import FactoryBus
from nn_bus import NNBus
from quantum_bus import QuantumBus
from system_output.exporter import SystemExporter
from safety_layer import SafetyLayer
from network_interface import NetworkInterface

class UnifiedBus:


    def __init__(self):
       
        self.safety = SafetyLayer()
        self.network = NetworkInterface()
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





#______step:technical evolution____________


from evolution_integration import evolution_cycle


class UnifiedBus:

    def __init__(self):
        ...
        self.evolution_log = []

    def cycle(self):

        ...

        # --- evolution trigger ---
        system_state = {
            "latency": 0.6,
            "entropy": q_state["entropy"]
        }

        evo = evolution_cycle(system_state)

        self.evolution_log.append(evo)

        self.exporter.log(f"NEW SUBSYSTEM: {evo['design']['name']}")

       ...