# factory_master.py

from factory_worker import FactoryWorker

class FactoryMaster:

    def __init__(self, ports):
        self.workers = [FactoryWorker(p) for p in ports]

    def start_cluster(self):
        for w in self.workers:
            w.start()