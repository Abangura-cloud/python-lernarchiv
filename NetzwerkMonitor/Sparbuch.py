from Konto import Konto 

class Sparbuch(Konto): 
    def __init__(self, kontonummer, inhaber, kontostand=0, zinssatz=0.02):
        super().__init__(kontonummer, inhaber, kontostand)
        self.zinssatz = zinssatz
    #===========================================================
    # Old: version 1
  #.  def zinsen_anwenden(self):
        # 🔒 Pull private balance via getter, calculate interest, and deposit it
  #.      aktuelle_balance = self.get_kontostand()
    #.     zinsen = aktuelle_balance * self.zinssatz
   #.     self.einzahlen(zinsen)

    #. def abheben(self, betrag):
        # 1. 🔒 Fetch private balance safely using the public Getter method
     #.   aktuelle_balance = self.get_kontostand()
        
        # 2. Check custom floor limit rule (Must keep at least 50 €)
     #.   if (aktuelle_balance - betrag) < 50:
     #.       raise ValueError("Sparbuch muss mindestens 50 Euro Guthaben behalten!")
        
        # 3. 🔑 Validation passed! Pass control up to parent class to securely subtract the money
    #.    super().abheben(betrag)
    #============================================================
    
    # New: Updated Version 2
    def zinsen_anwenden(self):
        # Read the property directly without using parentheses ()
        aktuelle_balance = self.kontostand
        zinsen = aktuelle_balance * self.zinssatz
        self.einzahlen(zinsen)

    def abheben(self, betrag):
        # Read the property directly without using parentheses ()
        if (self.kontostand - betrag) < 50:
            raise ValueError("Sparbuch muss mindestens 50 Euro Guthaben behalten!")
        
        super().abheben(betrag)

if __name__ == "__main__":
    print("--- Teste Encapsulated Sparbuch ---")
    mein_sparbuch = Sparbuch("DE123456", "Bang", 100)
    print(f"Konto erstellt für: {mein_sparbuch.inhaber}")
    print(f"Startguthaben: {mein_sparbuch.get_kontostand()} €")

    # 2. Test applying interest (100 * 0.02 = 2 Euro added)
    mein_sparbuch.zinsen_anwenden()
    print(f"Nach Zinsen: {mein_sparbuch.get_kontostand()} €")

    # 3. Test a valid withdrawal (leaves 52 Euro, which is > 50)
    mein_sparbuch.abheben(50)
    print(f"Nach Abhebung von 50€: {mein_sparbuch.get_kontostand()} €")

    # 4. Test the restriction rule (should trigger our ValueError)
    try:
        print("\nVersuche, zu viel abzuheben...")
        mein_sparbuch.abheben(10)
    except ValueError as e:
        print(f"Abgefangen! Fehler wie erwartet: {e}")
