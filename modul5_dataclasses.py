"""
Lernmodul 5: Dataclasses (`@dataclass`, `field`, `frozen=True`)
===============================================================
Key Takeaways:
1. `@dataclass` generiert automatisch `__init__`, `__repr__` und `__eq__` anhand von Type Hints.
2. Veränderliche Standardwerte (wie `list` oder `dict`) müssen über `field(default_factory=list)`
   erzeugt werden, damit nicht alle Instanzen dieselbe Liste teilen.
3. `@dataclass(frozen=True)` macht Instanzen unveränderlich (wirft `FrozenInstanceError` bei Änderungen).
"""

from dataclasses import dataclass, field, FrozenInstanceError


@dataclass(frozen=True)
class Produkt:
    name: str
    preis: float
    tags: list[str] = field(default_factory=list)


if __name__ == "__main__":
    p1 = Produkt("Mechanische Tastatur", 89.99)
    p2 = Produkt("Mechanische Tastatur", 89.99)

    print("Automatische __repr__:", p1)
    print("Automatische __eq__:", p1 == p2)

    p1.tags.append("USB-C")
    print("p1.tags:", p1.tags)
    print("p2.tags (eigene Liste):", p2.tags)

    try:
        p1.preis = 79.99
    except FrozenInstanceError as fehler:
        print(f"Unveränderlichkeit greift ({type(fehler).__name__}): {fehler}")

