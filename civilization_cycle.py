from software_civilization import SoftwareCivilization
from reality_simulation import RealitySimulation
from curiosity_engine import CuriosityEngine

boxes = [
    "A","B","C","D","E","F",
    "A1","B1","C1","D1","E1","F1",
    "Z","Z1","Y","Y1","X","X1"
]

civilization = SoftwareCivilization(boxes)
sim = RealitySimulation()
curiosity = CuriosityEngine()


def evolution_cycle():

    society = civilization.evolve_cycle()

    worlds = sim.run()
    best = sim.best_future()

    curiosity_event = curiosity.decide_exploration()

    return {
        "civilization": society,
        "best_future": best,
        "curiosity": curiosity_event
    }