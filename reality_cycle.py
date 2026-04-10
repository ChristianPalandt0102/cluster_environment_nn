from discovery_engine import DiscoveryEngine
from reality_compiler import RealityCompiler
from deployment_engine import DeploymentEngine
from network_engine import NetworkEngine

science = DiscoveryEngine()
compiler = RealityCompiler()
network = NetworkEngine()
deployer = DeploymentEngine(network)


def reality_cycle(knowledge):

    blueprint = compiler.compile(knowledge)

    result = deployer.deploy(blueprint)

    return {
        "blueprint": blueprint,
        "deployment": result
    }