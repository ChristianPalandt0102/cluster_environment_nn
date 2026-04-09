from neural_bus_controller import NeuralBusController

NN_CONTROLLER = NeuralBusController()

def neural_cycle():
    result = NN_CONTROLLER.cycle()
    print("[NN BUS]", result)

# factory_bus.py

from factory_master import FactoryMaster
from bus.config import BUS_CONFIG

class FactoryBus:

    def __init__(self):
        self.master = FactoryMaster(
            BUS_CONFIG["allowed_ports"][:30]
        )

    def boot(self):
        print("FactoryBus booting...")
        self.master.start_cluster()

    def benchmark(self):
        return {
            "workers": len(self.master.workers),
            "status": "running"
        }