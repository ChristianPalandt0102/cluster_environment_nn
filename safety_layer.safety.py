class SafetyLayer:

    def enforce(self, state, action):

        if action not in ["observe", "stabilize"]:
            return False, "blocked_action"

        return True, "ok"