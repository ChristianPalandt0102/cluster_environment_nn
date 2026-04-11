# self_writing_kernel_v3.py

from pathlib import Path
import time

SAFE_ZONE = Path("generated_modules")
SAFE_ZONE.mkdir(exist_ok=True)

from meta_compiler import MetaCompiler

self.compiler = MetaCompiler()
compiled_path = self.compiler.compile(mutation)

class SelfWritingKernel:

    def write_module(self, name, code):
        filename = SAFE_ZONE / f"{name}.py"

        wrapped = f"""
# AUTO GENERATED
# timestamp: {time.time()}

{code}
"""

        filename.write_text(wrapped)
        print(f"[Kernel] created {filename}")

    def validate(self, name):
        try:
            __import__(f"generated_modules.{name}")
            return True
        except Exception:
            return False