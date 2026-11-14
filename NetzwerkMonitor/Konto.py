class Konto:
    def __init__(self, kontonummer, inhaber, kontostand=0):
        self.kontonummer = kontonummer
        self.inhaber = inhaber
        # 1. 🔒 Make the variable private using a double underscore
        self.__kontostand = kontostand 
        
    #=======================================================
    # 2. 🔑 The public Getter method so child classes can read the balance safely
    # Old:  version:
    #def get_kontostand(self):
       # return self.__kontostand
        # 1. Add the property decorator right above the method
   #==========================================================

   # New: Updated version 
    @property
    def kontostand(self):
        """Securely exposes the private balance as a clean attribute."""
        return self.__kontostand


    def einzahlen(self, betrag):
        if betrag <= 0:
            raise ValueError("Betrag muss positiv sein!")
        self.__kontostand += betrag

    def abheben(self, betrag):
        if betrag > self.__kontostand:
            raise ValueError("Nicht genug Guthaben")
        self.__kontostand -= betrag


# Wrapping the test code here prevents it from interrupting other files during imports!
if __name__ == "__main__":
    print("--- Teste Konto Basisklasse ---")
    konto_a = Konto("DE001", "Anna Beispiel", 500)
    konto_b = Konto("DE002", "Ben Beispiel", 1200)

    # Dynamic Pay-In and Pay-Out inputs
    payIn = float(input('Please, Type pay-in amount: '))
    payOut = float(input('Please, Type pay-out amount: '))

    konto_a.einzahlen(payIn)
    konto_b.abheben(payOut)

    print(f"Konto A Stand: {konto_a.get_kontostand()} €")  
    print(f"Konto B Stand: {konto_b.get_kontostand()} €")  
