from evolution_compiler import EvolutionCompiler
from sandbox_genome_registry import GenomeRegistry
from adaptive_ring_router import AdaptiveRingRouter




from core_kernel import kernel
from factory_bus import FactoryBus
from quantum_bus import QuantumBus

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