# code_origin_engine.py

import random
import time
from pathlib import Path

CODEBASE = Path("generated_core")
CODEBASE.mkdir(exist_ok=True)


class CodeOriginEngine:

    def __init__(self):
        self.history = []

    def generate_module(self):

        name = f"module_{int(time.time())}"

        code = f"""
# AUTO-GENERATED MODULE

def evolve(x):
    return x * {round(random.uniform(0.8,1.2),3)}
"""

        return name, code

    def write(self, name, code):
        path = CODEBASE / f"{name}.py"
        path.write_text(code)
        self.history.append(name)
        return path

    def integrate(self, name):
        try:
            __import__(f"generated_core.{name}")
            return True
        except Exception:
            return False