"""
Übung: Ein eigener Decorator mit functools.wraps

Bearbeite die TODOs der Reihe nach. Details zu den einzelnen Teilaufgaben
stehen in der README.md.
"""

import functools
import time


def misst_zeit(label):
    """Decorator-Fabrik: erzeugt einen Decorator, der die Laufzeit
    der dekorierten Funktion misst und zusammen mit `label` ausgibt.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"[{label}] Dauer: {elapsed:.6f} Sekunden")
            return result
        return wrapper
    return decorator


@misst_zeit(label="Berechnung")
def berechne_summe(n):
    """Summiert alle Zahlen von 1 bis n."""
    ergebnis = 0
    for i in range(1, n + 1):
        ergebnis += i
    return ergebnis


if __name__ == "__main__":
    print("Ergebnis:", berechne_summe(1000))
    print("Name:", berechne_summe.__name__)
    print("Doc:", berechne_summe.__doc__)
