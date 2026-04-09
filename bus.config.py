# bus.config.py

BUS_CONFIG = {
    "routing_mode": "static",
    "buffer_limit_mbit": 256,
    "overflow_protection": True,
    "sync_interval": 2,
    "allowed_ports": list(range(3005, 3130))
}