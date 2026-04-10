import time
from exporter import SystemExporter

exp = SystemExporter()

def live_stream():

    while True:
        data = exp.collect_all()
        exp.stream(data)
        time.sleep(1)