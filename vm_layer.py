# vm_layer.py

class VirtualSandboxVM:

    def __init__(self, name):
        self.name = name
        self.memory_limit = "512MB"

    async def run(self, fn, *args):
        print(f"[VM:{self.name}] executing simulation")
        return await fn(*args)