class IdentityManager:

    def __init__(self, boxes):
        self.identities = {b: Identity(b) for b in boxes}

    def record(self, box, event):
        self.identities[box].remember(event)

    def bias(self, box):
        return self.identities[box].personality_bias()