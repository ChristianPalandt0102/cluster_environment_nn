from browser import document, timer
import random

console = document["console"]

def log(msg):
    console.text += f"\n{msg}"
    console.scrollTop = console.scrollHeight


# --- Simulated backend hooks ---

def run_cycle():
    result = {
        "nn_score": round(random.random(), 3),
        "decision": random.choice(["expand","mutate","stabilize"]),
        "agent": random.choice(["A","B","C","A1","Z"])
    }
    log(f"[CYCLE] {result}")


def evolve_system(ev):
    log("🧬 Evolution triggered")
    run_cycle()


def simulate(ev):
    log("🌌 Simulation running...")
    for i in range(3):
        run_cycle()


def start(ev):
    log("🚀 System started")
    timer.set_interval(lambda: run_cycle(), 2000)


log(f"[EVOLUTION] {data.get('evolution')}")

# --- Bind UI ---

document["start"].bind("click", start)
document["evolve"].bind("click", evolve_system)
document["simulate"].bind("click", simulate)