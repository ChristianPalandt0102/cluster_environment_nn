gpu_mind = ConsciousnessGPU()

def handle_packet(packet):

    intensity = packet.get("energy", 0.2)

    gpu_mind.signal_event(intensity)