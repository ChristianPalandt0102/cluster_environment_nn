class FactoryBus:

    def plan(self, nn_result):
        return [{"task": "compute"}]

    def execute(self, tasks):
        return [{"status": "done"}]