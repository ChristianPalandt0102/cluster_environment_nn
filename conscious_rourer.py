def quantum_choose(self, signal, operation_boxes):

    snapshot = operation_boxes.collect_snapshot()

    futures = operation_boxes.simulate_routes(snapshot)

    best = operation_boxes.evaluate(futures)

    return operation_boxes.collapse(best)