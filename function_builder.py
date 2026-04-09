# function_builder.py

import types
import hashlib


class FunctionBuilder:

    def __init__(self):
        self.registry = {}

    # --------------------------------
    def build(self, name, code_template):

        fn_hash = hashlib.sha256(code_template.encode()).hexdigest()[:10]

        namespace = {}

        exec(code_template, namespace)

        fn = None
        for v in namespace.values():
            if isinstance(v, types.FunctionType):
                fn = v

        if fn:
            self.registry[name] = fn
            print(f"[FUNC] built {name}:{fn_hash}")

        return fn

    # --------------------------------
    def execute(self, name, *args, **kwargs):
        if name not in self.registry:
            raise Exception("function not found")

        return self.registry[name](*args, **kwargs)