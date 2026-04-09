# quantum_bus.config.py

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