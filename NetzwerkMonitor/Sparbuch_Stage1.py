from Konto_Stage1 import KontoStage1

class SparbuchStage1(KontoStage1):
    def __init__(self, kontonummer, inhaber, kontostand=0, zinssatz=0.02):
        super().__init__(kontonummer, inhaber, kontostand)
        self.zinssatz = zinssatz

    def zinsen_anwenden(self):
        # 🔴 Directly modifying a public parent attribute
        self.kontostand += self.kontostand * self.zinssatz

    def abheben(self, betrag):
        if (self.kontostand - betrag) < 50:
            raise ValueError("Sparbuch muss mindestens 50 Euro Guthaben behalten!")
        super().abheben(betrag)

