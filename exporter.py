
# exporter.py

import json
import time
from pathlib import Path

from collectors.nn_collector import collect_nn
from collectors.cache_collector import collect_cache
from collectors.bus_collector import collect_bus
from collectors.agi_collector import collect_agi
from collectors.observer_collector import collect_observer
from collectors.quantum_collector import collect_quantum


OUTPUT_DIR = Path("system_output")
SNAPSHOT_DIR = OUTPUT_DIR / "snapshots"
STREAM_DIR = OUTPUT_DIR / "streams"
LOG_DIR = OUTPUT_DIR / "logs"

for d in [SNAPSHOT_DIR, STREAM_DIR, LOG_DIR]:
    d.mkdir(parents=True, exist_ok=True)


class SystemExporter:

    def __init__(self):
        self.history = []

    def collect_all(self):

        return {
            "timestamp": time.time(),
            "nn": collect_nn(),
            "cache": collect_cache(),
            "bus": collect_bus(),
            "agi": collect_agi(),
            "observer": collect_observer(),
            "quantum": collect_quantum()
        }

# inside exporter.collect_all()

"unified_bus": {
    "status": "active",
    "cycles": len(self.history)
}


    def snapshot(self):

        data = self.collect_all()
        name = f"snapshot_{int(time.time())}.json"

        path = SNAPSHOT_DIR / name
        path.write_text(json.dumps(data, indent=2))

        self.history.append(name)
        return path

    def stream(self, data):

        path = STREAM_DIR / "live_stream.json"
        path.write_text(json.dumps(data))

    def log(self, message):

        path = LOG_DIR / "system.log"
        with open(path, "a") as f:
            f.write(f"{time.time()} :: {message}\n")



