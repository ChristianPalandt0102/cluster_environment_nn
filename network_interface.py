# network_interface.py

import requests


class NetworkInterface:

    def __init__(self):
        self.sources = {
            "httpbin": "https://httpbin.org/get",
            "ip": "https://api.ipify.org?format=json"
        }

    def fetch(self, source="httpbin"):

        url = self.sources.get(source)

        try:
            r = requests.get(url, timeout=2)

            return {
                "status": r.status_code,
                "data": r.json()
            }

        except Exception as e:
            return {"error": str(e)}