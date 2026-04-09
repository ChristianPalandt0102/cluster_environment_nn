# upl_engine.py

import random
import string


class UPLEngine:

    def __init__(self):
        self.dictionary = {}
        self.reverse = {}

    def _symbol(self):
        return random.choice("ΞΣΩΔΨΛ") + str(random.randint(1, 99))

    def encode(self, meaning):

        if meaning not in self.reverse:
            symbol = self._symbol()
            self.dictionary[symbol] = meaning
            self.reverse[meaning] = symbol

        return self.reverse[meaning]

    def decode(self, symbol):
        return self.dictionary.get(symbol, "unknown")

    def compress(self, message):
        parts = message.split(":")
        encoded = [self.encode(p) for p in parts]
        return "|".join(encoded)

    def expand(self, encoded):
        parts = encoded.split("|")
        decoded = [self.decode(p) for p in parts]
        return ":".join(decoded)