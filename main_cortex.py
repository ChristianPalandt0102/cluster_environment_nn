
from hidden_layer_loop import HiddenLayerLoop


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