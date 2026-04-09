# signal_language.py

import random

class SignalLanguage:

    def __init__(self):
        self.dictionary = {}
        self.reverse = {}

    def invent(self, meaning):
        symbol = random.choice("ΣΩΔΨΛΞ") + str(random.randint(1,99))
        self.dictionary[symbol] = meaning
        self.reverse[meaning] = symbol
        return symbol

    def encode(self, meaning):
        if meaning not in self.reverse:
            return self.invent(meaning)
        return self.reverse[meaning]

    def decode(self, symbol):
        return self.dictionary.get(symbol, "unknown")


SIGNAL_LANGUAGE = SignalLanguage()