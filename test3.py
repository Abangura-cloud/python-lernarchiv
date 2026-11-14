class Konto:
    def __init__(self, inhaber, kontonummer, kontostand=0):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand

    def __repr__(self):
        return (f"Konto(inhaber={self.inhaber!r}, "
                f"kontonummer={self.kontonummer!r}, "
                f"kontostand={self.kontostand!r})")
Konto(inhaber='Anna Bauer', kontonummer='DE001', kontostand=500)