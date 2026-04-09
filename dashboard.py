
from browser import document, websocket
import json

term = document["terminal"]

def log(msg):
    term <= f"{msg}<br>"
    term.scrollTop = term.scrollHeight


# --- WEBSOCKET OBSERVER ---
ws = websocket.WebSocket("ws://localhost:8765")

@ws.bind("open")
def open(evt):
    log("[CONNECTED] observer stream")

@ws.bind("message")
def message(evt):
    data = json.loads(evt.data)

    log(f"[SIGNAL] {data}")

@ws.bind("close")
def close(evt):
    log("[DISCONNECTED]")



def message(evt):
    data = json.loads(evt.data)

    log(f"[SIGNAL] {data}")

    # send signal to JS world
    from browser import window
    window.dispatchEvent(
        window.CustomEvent.new(
            "sandbox_signal",
            {"detail": data}
        )
    )


# inside dashboard.py

from factory_bus import FACTORY
import json

def bench_endpoint():
    return json.dumps(FACTORY.benchmark())