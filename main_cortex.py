
from hidden_layer_loop import HiddenLayerLoop

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