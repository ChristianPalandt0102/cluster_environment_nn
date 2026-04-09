from curiosity_engine import CuriosityEngine
from artificial_physics_engine import ArtificialPhysicsEngine
from discovery_engine import DiscoveryEngine
from identity_layer import IdentityManager

boxes = ["A","B","C","D","E","F","A1","B1","C1","D1","E1","F1"]

curiosity = CuriosityEngine()
physics = ArtificialPhysicsEngine()
science = DiscoveryEngine()
identities = IdentityManager(boxes)


def scientific_cycle():

    curiosity_event = curiosity.decide_exploration()

    hypothesis = science.formulate_hypothesis(
        curiosity_event["question"]
    )

    physics.evolve_laws()

    experiment = science.experiment(physics)

    success = science.evaluate(experiment)

    knowledge = science.learn(hypothesis, success)

    identities.record("A", knowledge)

    return {
        "curiosity": curiosity_event,
        "experiment": experiment,
        "knowledge": knowledge
    }