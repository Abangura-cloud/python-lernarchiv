class Konto:
    def __init__(self, inhaber, kontonummer, kontostand=0):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand

a = Konto("Anna Bauer", "DE001", 500)
b = Konto("Anna Bauer", "DE001", 500)
print(a==b) # False
#print(konto)

# <__main__.Konto object at 0x0000022C7C6186E0>