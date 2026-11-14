# Stage 2: Private Encapsulation & Native Properties
class KontoStage2:
    def __init__(self, kontonummer, inhaber, kontostand=0):
        self.kontonummer = kontonummer
        self.inhaber = inhaber
        self.__kontostand = kontostand  

    @property
    def kontostand(self):
        return self.__kontostand

    def einzahlen(self, betrag):
        if betrag <= 0:
            raise ValueError("Betrag muss positiv sein!")
        self.__kontostand += betrag

    def abheben(self, betrag):
        if betrag > self.__kontostand:
            raise ValueError("Nicht genug Guthaben")
        self.__kontostand -= betrag
