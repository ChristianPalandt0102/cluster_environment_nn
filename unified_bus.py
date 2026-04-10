# unified_bus.py

from factory_bus import FactoryBus
from nn_bus import NNBus
from quantum_bus import QuantumBus
from system_output.exporter import SystemExporter
from safety_layer import SafetyLayer
from network_interface import NetworkInterface
from stream_gateway import StreamGateway
from stream_safety import StreamSafety
import asyncio
from fusion_engine import FusionEngine



class UnifiedBus:


    def __init__(self):
       
        self.safety = SafetyLayer()
        self.network = NetworkInterface()
        self.factory = FactoryBus()
        self.nn = NNBus()
        self.fusion = FusionEngine()
        self.quantum = QuantumBus()
        self.exporter = SystemExporter()
        self.stream = StreamGateway()
        self.stream_safety = StreamSafety()


    # --- CORE CYCLE ---

    def cycle(self):

        # 1. Gather system state
        q_state = self.quantum.sample_state()

        # 2. Neural evaluation
        nn_result = self.nn.process(q_state)

        # 3. Decide workload
        tasks = self.factory.plan(nn_result)

#_________Network introducement_________

    q_state = self.quantum.sample_state()

    # --- REAL NETWORK INPUT ---
    net_data = self.network.fetch("httpbin")

    nn_result = self.nn.process(q_state)

    tasks = self.factory.plan(nn_result)

    # --- SAFETY CHECK BEFORE EXECUTION ---
    safe, reason = self.safety.enforce(
        state={
            "latency": nn_result.get("score", 0),
            "entropy": q_state.get("entropy", 0)
        },
        action="compute"
    )

    if not safe:
        self.exporter.log(f"[BLOCKED] {reason}")
        return {"status": "blocked", "reason": reason}

    results = self.factory.execute(tasks)

    # --- SAFE EVOLUTION ---
    evo = evolution_cycle({
        "latency": nn_result.get("score", 0),
        "entropy": q_state.get("entropy", 0)
    })

    code_safe, code_reason = self.safety.validate_code(
        evo["design"]["name"]
    )

    if not code_safe:
        self.exporter.log(f"[CODE BLOCKED] {code_reason}")
    else:
        self.evolution_log.append(evo)

    data = {
        "quantum": q_state,
        "nn": nn_result,
        "network": net_data,
        "results": results
    }

    self.exporter.stream(data)

    return data


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
    q_state = self.quantum.sample_state()

    # --- STREAM DATA ---
    raw_stream = self.stream.get_latest()
    safe_stream = self.stream_safety.filter(raw_stream)

    # feed into NN
    nn_result = self.nn.process({
        "quantum": q_state,
        "stream": safe_stream
    })

    tasks = self.factory.plan(nn_result)

    # SAFETY CHECK
    safe, reason = self.safety.enforce(
        state={
            "latency": nn_result.get("score", 0),
            "entropy": q_state.get("entropy", 0)
        },
        action="analyze"
    )

    if not safe:
        return {"status": "blocked", "reason": reason}

    results = self.factory.execute(tasks)

    data = {
        "quantum": q_state,
        "stream": safe_stream,
        "nn": nn_result,
        "results": results
    }

    self.exporter.stream(data)

    return data
        return data


async def start_streams(bus):

    await asyncio.gather(
        bus.stream.connect(
            "btc",
            "wss://stream.binance.com:9443/ws/btcusdt@trade"
        ),
        bus.stream.connect(
            "echo",
            "wss://echo.websocket.events"
        )
    )




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