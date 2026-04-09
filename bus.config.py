# bus.config.py


from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Field:
    name: str
    port_range: range
    workers_per_port: int
    processes_per_worker: int
    subprocesses: int


@dataclass
class BusConfig:

    version: str = "BUS-CORE-2.0"

    # Server routing ports
    main_port_range: range = range(3100, 3130)

    fields: Dict[str, Field] = field(default_factory=lambda: {

        # Primary evolution field
        "A_to_F_field": Field(
            name="A_to_F_field",
            port_range=range(3100, 3112),
            workers_per_port=1,
            processes_per_worker=3,
            subprocesses=10
        ),

        # Mirror recovery field
        "B_to_E1_field": Field(
            name="B_to_E1_field",
            port_range=range(3112, 3120),
            workers_per_port=1,
            processes_per_worker=3,
            subprocesses=10
        ),

        # Z-range experimental sandboxes
        "Z_Y_X_field": Field(
            name="Z_Y_X_field",
            port_range=range(3120, 3126),
            workers_per_port=1,
            processes_per_worker=3,
            subprocesses=10
        ),

        # Operation boxes (quantum research VM)
        "operation_boxes": Field(
            name="operation_boxes",
            port_range=range(3126, 3130),
            workers_per_port=2,
            processes_per_worker=3,
            subprocesses=10
        ),
    })

    # Memory systems attached
    memory_domains = {
        "L5_cache": True,
        "gpu_buffer_32bit": True,
        "integration_cache_8bit": True
    }

    # System observers
    observers = [
        "observer_engine",
        "network_engine",
        "self_writing_kernel"
    ]

    # Failover strategy
    failover = {
        "mode": "state_mirror",
        "backup_sync": True,
        "auto_rebuild": True
    }


# global instance
SYSTEM_BUS = BusConfig()




BUS_CONFIG = {
    "routing_mode": "static",
    "buffer_limit_mbit": 256,
    "overflow_protection": True,
    "sync_interval": 2,
    "allowed_ports": list(range(3005, 3130))
}