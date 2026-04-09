from evolution_compiler import EvolutionCompiler
from sandbox_genome_registry import GenomeRegistry
from adaptive_ring_router import AdaptiveRingRouter
from core_kernel import kernel
from factory_bus import FactoryBus
from quantum_bus import QuantumBus

from observer_engine import ObserverEngine
from hidden_layer_loop import HiddenLayerLoop
from sandbox_dna_compiler import SandboxDNA
from neural_router import NeuralRouter
from observer_ws_stream import run_stream
import threading

# ---- LOAD DNA ----
dna = SandboxDNA()
profile = dna.compile_runtime_profile()

# ---- OBSERVER ----
observer = ObserverEngine()
observer.register_subnetwork(dna.client_id)

# ---- ROUTER ----
router = NeuralRouter(observer)
router.register_node("A", dna.ports)
router.register_node("A1", dna.ports)

# ---- HIDDEN LAYER ----
hidden = HiddenLayerLoop(observer)
hidden.start()

# ---- WEBSOCKET DASHBOARD ----
threading.Thread(
    target=run_stream,
    args=(observer,),
    daemon=True
).start()

# ---- SIMULATED TRAFFIC ----
import time
while True:
    router.adaptive_route({"task": "compute"})
    time.sleep(3)

factory = FactoryBus()
qbus = QuantumBus()

kernel.register_node("factory", factory)
kernel.register_node("quantum", qbus)

factory.boot()

kernel.heartbeat()





# dream engine assumed existing
compiler = EvolutionCompiler(dream_engine)

genomes = GenomeRegistry()
for box in ["A","B","C","D","E","F","A1","B1","C1","D1","E1","F1"]:
    genomes.register(box)

router = AdaptiveRingRouter(list(genomes.genomes.keys()))

# evolution loop
def evolution_cycle():
    compiler.cycle()
    genomes.evolve({
        "throughput": 0.8,
        "latency": 0.2
    })

    print(router.route("A"))