# Stage 1: Public Attributes (No protection)
class KontoStage1:
    def __init__(self, kontonummer, inhaber, kontostand=0):
        self.kontonummer = kontonummer
        self.inhaber = inhaber
        self.kontostand = kontostand  

    def einzahlen(self, betrag):
        self.kontostand += betrag

    def abheben(self, betrag):
        if betrag > self.kontostand:
            raise ValueError("Nicht genug Guthaben")
        self.kontostand -= betrag
