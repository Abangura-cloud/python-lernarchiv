"""
Lernmodul 5: Eigene Context Manager (`with`-Statement)
======================================================
Key Takeaways:
1. Klassenbasierter Context Manager implementiert `__enter__` (Öffnen) und `__exit__` (Aufräumen).
2. `__exit__` wird IMMER ausgeführt, auch wenn im `with`-Block ein Fehler auftritt.
3. Gibt `__exit__` `False` (oder `None`) zurück, wird eine Exception normal nach außen weitergegeben.
4. `@contextmanager` aus `contextlib` erlaubt dieselbe Logik kompakt mit `try ... yield ... finally`.
"""

from contextlib import contextmanager


class DatenbankVerbindung:
    """Klassenbasierter Context Manager für komplexere Ressourcen und Zustand."""

    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"[Klasse] Verbindung zu '{self.name}' geöffnet.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"[Klasse] Verbindung zu '{self.name}' geschlossen.")
        return False


@contextmanager
def datenbank_verbindung(name: str):
    """Generatorbasierter Context Manager für schlanke Setup/Teardown-Abläufe."""
    print(f"[@contextmanager] Verbindung zu '{name}' geöffnet.")
    try:
        yield name
    finally:
        print(f"[@contextmanager] Verbindung zu '{name}' geschlossen.")


if __name__ == "__main__":
    with DatenbankVerbindung("kunden_db") as db:
        print("Abfrage läuft auf:", db.name)

    print()

    try:
        with datenbank_verbindung("bestell_db") as db_name:
            print("Abfrage läuft auf:", db_name)
            raise ValueError("Ungültige SQL-Abfrage")
    except ValueError as fehler:
        print("Fehler sauber außerhalb abgefangen:", fehler)

