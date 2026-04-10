import asyncio
from core.unified_bus import UnifiedBus
from stream.stream_gateway import StreamGateway

bus = UnifiedBus()

async def main():

    # start streams
    asyncio.create_task(
        bus.stream.connect(
            "btc",
            "wss://stream.binance.com:9443/ws/btcusdt@trade"
        )
    )

    while True:
        data = bus.cycle()
        print("[TSN]", data)
        await asyncio.sleep(1)

asyncio.run(main())