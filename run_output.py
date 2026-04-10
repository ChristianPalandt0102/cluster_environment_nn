# run_output.py

import time
from exporter import SystemExporter

exp = SystemExporter()

while True:

    data = exp.collect_all()

    exp.stream(data)
    exp.log("cycle complete")

    if int(time.time()) % 10 == 0:
        exp.snapshot()

    time.sleep(1)