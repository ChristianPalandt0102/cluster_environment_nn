

class AdaptiveRing:

    def __init__(self, nodes):
        self.nodes = nodes
        self.activity = {n:0 for n in nodes}

    def signal(self, node):
        self.activity[node] += 1

    def rewire(self):

        # sort by activity
        ordered = sorted(
            self.activity,
            key=lambda n:self.activity[n],
            reverse=True
        )

        self.nodes = ordered
        print("[ROUTING] ring evolved:", self.nodes)


gpu_mind = ConsciousnessGPU()

def handle_packet(packet):

    intensity = packet.get("energy", 0.2)

    gpu_mind.signal_event(intensity)