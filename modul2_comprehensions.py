"""
Modul 2 (Ergänzung): Comprehensions, map/filter und Lambda-Regeln.
"""

# 1. List Comprehension mit Filter (Trailing if)
zahlen = [3, 8, 12, 5, 17, 24, 9, 16]
ungerade_quadrate = [z ** 2 for z in zahlen if z % 2 != 0]

# 2. List Comprehension mit Transformation (if-else vorne: alle Elemente bleiben erhalten)
gerade_oder_null = [z ** 2 if z % 2 == 0 else 0 for z in zahlen]

# 3. Dictionary Comprehension aus zwei Listen
produkte = ["Apfel", "Brot", "Milch", "Käse"]
preise = [0.5, 2.3, 1.1, 3.4]
preisliste = {produkte[i]: preise[i] for i in range(len(produkte))}

# 4. Set Comprehension (keine Doppelpunkte -> erzeugt ein Set, kein Dict!)
woerter = ["Apfel", "Birne", "Kiwi", "Erbse", "Ananas", "Traube"]
anfangsbuchstaben = {wort[0] for wort in woerter}

# 5. Verschachtelte Comprehension (gleiche Reihenfolge wie verschachtelte for-Schleifen)
matrix = [
    [4, -2, 7, 15],
    [-9, 3, 22, -6],
]
positive_quadrate = [zahl ** 2 for zeile in matrix for zahl in zeile if zahl > 0]

# 6. Vergleich: map + filter + lambda vs. Comprehension
# Hinweis: Eine lambda-Funktion darf NUR einen einzigen Ausdruck enthalten (keine for-Schleife).
# Laut PEP 8 sollten lambdas nur anonym (z. B. als key=...) genutzt und nicht Variablen zugewiesen werden.
map_filter_ergebnis = list(map(lambda z: z ** 2, filter(lambda z: z % 2 == 0, zahlen)))

if __name__ == "__main__":
    print("1. Ungerade Quadrate:", ungerade_quadrate)
    print("2. Gerade oder 0:    ", gerade_oder_null)
    print("3. Preisliste (Dict):", preisliste)
    print("4. Buchstaben (Set): ", anfangsbuchstaben)
    print("5. Matrix-Quadrate:  ", positive_quadrate)
    print("6. map + filter:     ", map_filter_ergebnis)
