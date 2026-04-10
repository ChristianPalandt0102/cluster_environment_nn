# observer/dashboard.py

from aiohttp import web
import os

BASE = os.path.dirname(__file__)

async def index(request):
    return web.FileResponse(f"{BASE}/static/index.html")

app = web.Application()
app.router.add_get("/", index)
app.router.add_static("/", f"{BASE}/static")

if __name__ == "__main__":
    print("Dashboard running:")
    print("http://localhost:8080")

    web.run_app(app, port=8080)
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

log(f"[NETWORK] {data.get('network')}")
log(f"[SAFETY] {data.get('status', 'ok')}")



# inside dashboard.py

from factory_bus import FACTORY
import json

def bench_endpoint():
    return json.dumps(FACTORY.benchmark())

from browser import ajax
import json

def fetch_data():

    def on_complete(req):
        data = json.loads(req.text)
        log(f"[LIVE] {data['agi']}")

    req = ajax.ajax()
    req.bind('complete', on_complete)
    req.open('GET', '/streams/live_stream.json', True)
    req.send()
def fetch_data():

    def on_complete(req):
        data = json.loads(req.text)

        if "stream" in data:
            log(f"[STREAM] {data['stream'][-1]}")

    req = ajax.ajax()
    req.bind('complete', on_complete)
    req.open('GET', '/streams/live_stream.json', True)
    req.send()