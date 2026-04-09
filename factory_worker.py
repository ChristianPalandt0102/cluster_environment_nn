# factory_worker.py

import multiprocessing as mp

class FactoryWorker:

    def __init__(self, port):
        self.port = port
        self.processes = []

    def start(self):
        for _ in range(3):  # 3 processes per port
            p = mp.Process(target=self.process_loop)
            p.start()
            self.processes.append(p)

    def process_loop(self):
        for _ in range(10):  # 10 subprocess simulations
            self.execute_task()

    def execute_task(self):
        print(f"[Worker:{self.port}] task executed")