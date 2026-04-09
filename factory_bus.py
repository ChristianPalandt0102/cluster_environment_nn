from neural_bus_controller import NeuralBusController

from evolution_engine import EVOLUTION_ENGINE
from factory_master import FactoryMaster
from bus.config import BUS_CONFIG



def execute(self, task):
    dna = EVOLUTION_ENGINE.population.get(self.wid)
    delay = dna.sleep_factor if dna else 0.01

    time.sleep(delay)


NN_CONTROLLER = NeuralBusController()

def neural_cycle():
    result = NN_CONTROLLER.cycle()
    print("[NN BUS]", result)

# factory_bus.py

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