import functools
import time


def misst_zeit(label):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"[{label}] '{func.__name__}' dauerte {elapsed:.6f} Sekunden.")
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
    # Aufruf der Funktion, damit die Zeitmessung startet
    summe = berechne_summe(1000)
    print("Ergebnis:", summe)

    # Überprüfung der Metadaten
    print("Name:", berechne_summe.__name__)
    print("Doc:", berechne_summe.__doc__)

    # Erklärung zu Teilaufgabe 3 (Beobachtung ohne functools.wraps):
    # Ohne @functools.wraps(func) geben __name__ "wrapper" und __doc__ None zurück,
    # weil der Dekorator die innere Funktion wrapper zurückgibt und der Name berechne_summe
    # nach der Dekoration auf dieses wrapper-Objekt verweist statt auf die Originalfunktion.
