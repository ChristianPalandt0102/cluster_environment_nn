import pickle
from exporter import SystemExporter

exp = SystemExporter()

def export_binary():

    data = exp.collect_all()

    with open("system_output/snapshots/data.bin", "wb") as f:
        pickle.dump(data, f)