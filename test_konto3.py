class Konto:
    def __init__(self, inhaber, kontonummer, kontostand=0):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand
        self._transaktionen = []

    def einzahlen(self, betrag):
        self.kontostand += betrag
        self._transaktionen.append(betrag)

    def abheben(self, betrag):
        self.kontostand -= betrag
        self._transaktionen.append(-betrag)

    def __repr__(self):
        return (f"Konto(inhaber={self.inhaber!r}, "
                f"kontonummer={self.kontonummer!r}, "
                f"kontostand={self.kontostand!r})")

    def __eq__(self, other):
        if not isinstance(other, Konto):
            return NotImplemented
        return (self.kontonummer == other.kontonummer
                and self.kontostand == other.kontostand)

    def __iter__(self):
        return iter(self._transaktionen)
konto = Konto("Anna Bauer", "DE001", 500)
konto.einzahlen(200)
konto.abheben(50)

for betrag in konto:
    print(betrag)
