antwortzeiten_ms = [45, 120, 88, 250, 99, 310, 60]

# Weg 1: Mit filter() und map() + lambda
langsame_zeiten = list(filter(lambda ms: ms > 100, antwortzeiten_ms))
warnungen_functional = list(map(lambda ms: f"WARNUNG: {ms}ms", langsame_zeiten))

# Weg 2: Mit einer einzigen List Comprehension (Der Pythonic Way!)
# TODO 1: Write a list comprehension that produces the exact same list as 'warnungen_functional'
# Hint: [f"WARNUNG: {ms}ms" for ms in antwortzeiten_ms if ...]
warnungen_comprehension = [f"WARNUNG: {ms}ms" for ms in antwortzeiten_ms if ms > 100]

# Bonus: Dictionary Comprehension
# TODO 2: Create a dict mapping each slow response time (ms > 100) to its value in seconds (ms / 1000)
#zeiten_in_sekunden = {ms: ms / 1000 for ms in antwortzeiten_ms if ms > 100}

# Example format: {120: 0.12, 250: 0.25, 310: 0.31}
zeiten_in_sekunden = {ms: ms / 1000 for ms in antwortzeiten_ms if ms > 100}


if __name__ == "__main__":
    print("Functional:   ", warnungen_functional)
    print("Comprehension:", warnungen_comprehension)
    print("Sekunden-Dict:", zeiten_in_sekunden)
