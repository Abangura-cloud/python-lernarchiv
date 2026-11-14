class Bibliothek:
    buecher = []

    def hinzufuegen(self, titel):
        self.buecher.append(titel)

a = Bibliothek()
b = Bibliothek()
a.hinzufuegen("Buch A")
b.hinzufuegen("Buch B")
print(len(a.buecher))
print(len(b.buecher))