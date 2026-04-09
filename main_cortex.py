
from hidden_layer_loop import HiddenLayerLoop


scheduler = KernelScheduler(grid, cache)
memory = TemporalMemory()
research = ResearchAgent(operation_boxes, memory)

async def cognitive_cycle():

    while True:

        scheduler.cycle()

        state = scheduler.observe()
        memory.recall_similar(state)

        await research.run_experiment()

        await asyncio.sleep(5)


energy = EnergyModel(grid)
consensus = ConsensusCore(grid, energy)
genesis = GenesisLanguage()

async def governance_cycle():

    while True:

        instruction = genesis.generate_instruction()

        if consensus.decide(instruction):
            genesis.interpret(instruction, kernel)

        await asyncio.sleep(8)



hidden_layer = HiddenLayerLoop(
    dream_engine,
    class_builder,
    temporal_memory,
    consensus,
    energy
)

asyncio.create_task(hidden_layer.cycle())

if msg["type"] == "template_mutation":
    template_db.integrate(msg["template"])