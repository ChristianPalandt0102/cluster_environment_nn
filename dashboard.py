
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