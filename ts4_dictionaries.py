woerter = ["Katze", "Elefant", "Hund", "Nilpferd"]
laengen = {wort: len(wort) for wort in woerter}
print(laengen)

print("=========")
vorkommende_laengen = {len(wort) for wort in woerter}
print(vorkommende_laengen)