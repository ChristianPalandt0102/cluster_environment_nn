import asyncio
from unified_bus import UnifiedBus, start_streams

bus = UnifiedBus()

async def main():

    asyncio.create_task(start_streams(bus))

    while True:
        data = bus.cycle()
        print("[LIVE]", data)
        await asyncio.sleep(1)

asyncio.run(main())