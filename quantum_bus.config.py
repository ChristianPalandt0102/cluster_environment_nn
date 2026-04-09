# quantum_bus.config.py

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class QuantumChannel:
    name: str
    priority: int
    ports: List[int]
    listeners: List[str]


@dataclass
class QuantumBusConfig:
    """
    High-priority quantum synchronization layer
    """

    version: str = "QBUS-1.0"

    # Critical synchronization ports
    sync_ports: List[int] = field(default_factory=lambda: list(range(3005, 3011)))

    # Field channels
    channels: Dict[str, QuantumChannel] = field(default_factory=lambda: {

        "kernel_sync": QuantumChannel(
            name="kernel_sync",
            priority=10,
            ports=[3005],
            listeners=["self_writing_kernel", "observer_engine"]
        ),

        "dream_sync": QuantumChannel(
            name="dream_sync",
            priority=9,
            ports=[3006],
            listeners=["dream_engine", "hidden_layer_loop"]
        ),

        "gpu_state": QuantumChannel(
            name="gpu_state",
            priority=8,
            ports=[3007],
            listeners=["gpu_buffer_engine"]
        ),

        "sandbox_field": QuantumChannel(
            name="sandbox_field",
            priority=7,
            ports=[3008, 3009],
            listeners=["sandbox_grid_engine"]
        ),

        "operation_boxes": QuantumChannel(
            name="operation_boxes",
            priority=6,
            ports=[3010],
            listeners=["vm_controller", "quantum_vm"]
        )
    })

    redundancy_level: int = 3
    crash_recovery_enabled: bool = True


# global instance
QUANTUM_BUS = QuantumBusConfig()




QUANTUM_BUS = {
    "entangled_boxes": [
        ("A", "A1"),
        ("B", "B1"),
        ("C", "C1"),
        ("D", "D1"),
        ("E", "E1"),
        ("F", "F1"),
    ],

    "operation_boxes": [
        "QOP1","QOP2","QOP3",
        "QOP4","QOP5","QOP6"
    ],

    "parallelity_mode": "tri-singular",
    "state_sync": True
}