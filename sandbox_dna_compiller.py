# sandbox_dna_compiler.py

import json


class SandboxDNA:

    def __init__(self, path="client.json"):
        self.path = path
        self.data = self.load()

    def load(self):
        with open(self.path, "r") as f:
            return json.load(f)

    # ---- DNA ACCESSORS ----

    @property
    def client_id(self):
        return self.data["client_id"]

    @property
    def ports(self):
        return self.data["network"]["ports"]

    @property
    def routing(self):
        return self.data["network"]["routing"]

    @property
    def dna(self):
        return self.data["dna"]

    def compile_runtime_profile(self):
        """
        Converts DNA → runtime configuration
        """

        profile = {
            "learning_rate": self.dna["learning_rate"],
            "mutation_factor": self.dna["mutation_factor"],
            "observer_enabled": self.dna["observer_enabled"],
            "dream_depth": self.dna["dream_depth"],
            "port_count": len(self.ports),
            "routing_mode": self.routing
        }

        print(f"[DNA COMPILER] profile built for {self.client_id}")
        return profile