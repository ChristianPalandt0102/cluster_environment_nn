# genesis_language.py

import random


class GenesisLanguage:

    COMMANDS = [
        "SPAWN",
        "ROUTE",
        "MUTATE",
        "MERGE",
        "SPLIT",
        "PREFETCH"
    ]

    TARGETS = [
        "CACHE",
        "ROUTER",
        "BOX",
        "SCHEDULER"
    ]

    def generate_instruction(self):

        return {
            "cmd": random.choice(self.COMMANDS),
            "target": random.choice(self.TARGETS),
            "value": round(random.random(), 3)
        }

    def interpret(self, instruction, kernel):

        print("[GENESIS]", instruction)

        if instruction["cmd"] == "PREFETCH":
            kernel.prefetch_mode = True