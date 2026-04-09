# upl_agent.py

from upl_engine import UPLEngine
from protocol_evolution import ProtocolEvolution

upl = UPLEngine()
evo = ProtocolEvolution()


class UPLAgent:

    def __init__(self, name):
        self.name = name

    def send(self, message):
        encoded = upl.compress(message)
        evo.record(encoded)
        return encoded

    def receive(self, encoded):
        return upl.expand(encoded)