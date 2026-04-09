# inside dashboard.py

from factory_bus import FACTORY
import json

def bench_endpoint():
    return json.dumps(FACTORY.benchmark())