class Konto:
    def __init__(self, inhaber, kontonummer, kontostand=0):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand

    def __repr__(self):
        return (f"Konto(inhaber={self.inhaber!r}, "
                f"kontonummer={self.kontonummer!r}, "
                f"kontostand={self.kontostand!r})")

    def __eq__(self, other):
        if not isinstance(other, Konto):
            return NotImplemented
        return (self.kontonummer == other.kontonummer
                and self.kontostand == other.kontostand)
a = Konto("Anna Bauer", "DE001", 500)
b = Konto("Anna Bauer", "DE001", 500)
print(a==b)