from Konto_Stage2 import KontoStage2

class SparbuchStage2(KontoStage2):
    def __init__(self, kontonummer, inhaber, kontostand=0, zinssatz=0.02):
        super().__init__(kontonummer, inhaber, kontostand)
        self.zinssatz = zinssatz

    def zinsen_anwenden(self):
        # 🔒 Safely reading via property, then changing it via the safe deposit method
        zinsen = self.kontostand * self.zinssatz
        self.einzahlen(zinsen)

    def abheben(self, betrag):
        if (self.kontostand - betrag) < 50:
            raise ValueError("Sparbuch muss mindestens 50 Euro Guthaben behalten!")
        super().abheben(betrag)

