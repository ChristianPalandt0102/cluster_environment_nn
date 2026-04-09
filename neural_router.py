# neural_router.py

import random
import time


class NeuralRouter:

    def __init__(self, observer):
        self.observer = observer
        self.nodes = []
        self.routing_index = 0

    def register_node(self, name, ports):
        self.nodes.append({
            "name": name,
            "ports": ports,
            "health": 1.0
        })

    def next_node(self):
        if not self.nodes:
            return None

        node = self.nodes[self.routing_index]
        self.routing_index = (self.routing_index + 1) % len(self.nodes)
        return node

    def adaptive_route(self, payload):
        node = self.next_node()

        if not node:
            return None

        selected_port = random.choice(node["ports"])

        route_info = {
            "target": node["name"],
            "port": selected_port,
            "payload": payload
        }

        self.observer.observe({
            "mutation": "route",
            "route": route_info
        })

        print(f"[ROUTER] → {node['name']}:{selected_port}")

        return route_info

    def degrade_node(self, name, factor=0.1):
        for n in self.nodes:
            if n["name"] == name:
                n["health"] -= factor