class ControllerEngine:

    def decide(self, anomaly, nn):
        if anomaly.get("anomaly"):
            return {"action": "stabilize"}
        return {"action": "observe"}

    def apply(self, action, system):
        return action