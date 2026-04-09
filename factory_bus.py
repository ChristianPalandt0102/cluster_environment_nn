from neural_bus_controller import NeuralBusController

NN_CONTROLLER = NeuralBusController()

def neural_cycle():
    result = NN_CONTROLLER.cycle()
    print("[NN BUS]", result)