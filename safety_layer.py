# safety_layer.py

import time


class SafetyLayer:

    def __init__(self):

        self.rules = {
            "max_latency": 0.9,
            "max_entropy": 0.95,
            "allowed_actions": [
                "compute", "optimize", "analyze", "simulate"
            ],
            "blocked_modules": [
                "self_delete", "external_exec"
            ]
        }

        self.violation_log = []

    # --- VALIDATE SYSTEM STATE ---
    def validate_state(self, state):

        if state.get("latency", 0) > self.rules["max_latency"]:
            return False, "latency_limit_exceeded"

        if state.get("entropy", 0) > self.rules["max_entropy"]:
            return False, "entropy_limit_exceeded"

        return True, "ok"

    # --- VALIDATE ACTION ---
    def validate_action(self, action):

        if action not in self.rules["allowed_actions"]:
            return False, "action_not_allowed"

        return True, "ok"

    # --- VALIDATE GENERATED CODE ---
    def validate_code(self, code):

        blocked = self.rules["blocked_modules"]

        for b in blocked:
            if b in code:
                return False, f"blocked_pattern:{b}"

        return True, "safe"

    # --- ENFORCE ---
    def enforce(self, state, action, code=None):

        ok_state, s_msg = self.validate_state(state)
        ok_action, a_msg = self.validate_action(action)

        if code:
            ok_code, c_msg = self.validate_code(code)
        else:
            ok_code, c_msg = True, "no_code"

        if not (ok_state and ok_action and ok_code):

            violation = {
                "time": time.time(),
                "state": s_msg,
                "action": a_msg,
                "code": c_msg
            }

            self.violation_log.append(violation)

            return False, violation

        return True, "approved"