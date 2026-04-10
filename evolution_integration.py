from tech_evolution_engine import TechEvolutionEngine
from code_origin_engine import CodeOriginEngine

tech = TechEvolutionEngine()
origin = CodeOriginEngine()


def evolution_cycle(system_state):

    design, code = tech.evolve(system_state)

    path = origin.write(design["name"], code)

    integrated = origin.integrate(design["name"])

    return {
        "design": design,
        "path": str(path),
        "integrated": integrated
    }