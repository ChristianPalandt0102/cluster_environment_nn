import asyncio
from sandbox_grid_engine import SandboxGridEngine
from function_builder import FunctionBuilder

grid = SandboxGridEngine()
builder = FunctionBuilder()


# -----------------------
# BOX DEFINITIONS
# -----------------------

async def box_Z(signal):
    print("[Z] received", signal.type)

    if signal.type == "DISCOVER":
        grid.emit("Z", "Z1", {"msg": "wake"}, "SYNC")


async def box_Z1(signal):
    print("[Z1] processing", signal.payload)


# register start nodes
grid.register_box("Z", box_Z)
grid.register_box("Z1", box_Z1)


async def main():
    asyncio.create_task(grid.dispatcher())

    # boot impulse
    grid.emit("SYSTEM", "Z", {}, "DISCOVER")

    while True:
        await asyncio.sleep(1)

asyncio.run(main())