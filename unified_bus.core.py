from buses.factory_bus import FactoryBus
from buses.nn_bus import NNBus
from buses.quantum_bus import QuantumBus

from stream.stream_gateway import StreamGateway
from stream.stream_safety import StreamSafety

from fusion.fusion_engine import FusionEngine
from intelligence.anomaly_engine import AnomalyEngine
from intelligence.controller_engine import ControllerEngine

from safety.safety_layer import SafetyLayer
from output.exporter import SystemExporter


class UnifiedBus:

    def __init__(self):

        self.factory = FactoryBus()
        self.nn = NNBus()
        self.quantum = QuantumBus()

        self.stream = StreamGateway()
        self.stream_safety = StreamSafety()
        self.fusion = FusionEngine()

        self.anomaly = AnomalyEngine()
        self.controller = ControllerEngine()

        self.safety = SafetyLayer()
        self.exporter = SystemExporter()

    def cycle(self):

        q_state = self.quantum.sample_state()

        raw_stream = self.stream.get_latest()
        safe_stream = self.stream_safety.filter(raw_stream)

        fused = self.fusion.fuse(safe_stream)

        anomaly = self.anomaly.detect(fused)

        nn_result = self.nn.process({
            "fusion": fused,
            "quantum": q_state
        })

        decision = self.controller.decide(anomaly, nn_result)
        self.controller.apply(decision["action"], self)

        safe, reason = self.safety.enforce(
            {"latency": nn_result.get("score", 0)},
            decision["action"]
        )

        if not safe:
            return {"status": "blocked", "reason": reason}

        tasks = self.factory.plan(nn_result)
        results = self.factory.execute(tasks)

        data = {
            "fusion": fused,
            "anomaly": anomaly,
            "decision": decision,
            "results": results
        }

        self.exporter.stream(data)

        return data