import time
from unified_bus import UnifiedBus

bus = UnifiedBus()

while True:

    data = bus.cycle()

    print("[CYCLE]", data)

    time.sleep(1)