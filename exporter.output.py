import json, pathlib

class SystemExporter:

    def __init__(self):
        self.path = pathlib.Path("output/live.json")

    def stream(self, data):
        self.path.write_text(json.dumps(data))