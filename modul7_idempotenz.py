"""
Modul 7 – Referenz: Idempotente Skripte für wiederkehrende Aufgaben (Cron / Task Scheduler)
"""

from datetime import date
from pathlib import Path

LOG_DATEI = Path(__file__).parent / "idempotenz_lauf.log"


def eintrag_fuer_datum(stichtag: date) -> str:
    """Erzeugt eine standardisierte, datierte Logzeile im ISO-8601-Format."""
    return f"{stichtag.isoformat()}: Tägliche Prüfung erfolgreich durchgeführt"


def eintrag_existiert_bereits(log_pfad: Path, stichtag: date) -> bool:
    """Prüft zustandsbasiert, ob für den Stichtag bereits ein Eintrag vorliegt."""
    if not log_pfad.exists():
        return False

    praefix = f"{stichtag.isoformat()}:"
    inhalt = log_pfad.read_text(encoding="utf-8")
    return any(zeile.startswith(praefix) for zeile in inhalt.splitlines())


def idempotenter_lauf(log_pfad: Path, stichtag: date | None = None) -> bool:
    """Führt den Lauf nur aus, wenn für das Datum noch kein Eintrag existiert.

    Gibt True zurück, wenn ein neuer Eintrag geschrieben wurde, sonst False.
    """
    ziel_datum = stichtag or date.today()
    if eintrag_existiert_bereits(log_pfad, ziel_datum):
        print(f"[SKIP] Eintrag für {ziel_datum.isoformat()} existiert bereits.")
        return False

    log_pfad.parent.mkdir(parents=True, exist_ok=True)
    zeile = eintrag_fuer_datum(ziel_datum)
    with log_pfad.open("a", encoding="utf-8") as datei:
        datei.write(f"{zeile}\n")
    print(f"[OK]   Neuer Eintrag geschrieben: {zeile}")
    return True


def main() -> None:
    if LOG_DATEI.exists():
        LOG_DATEI.unlink()

    heute = date.today()
    print("=== Simulation: 3-facher Start am selben Tag ===")
    for lauf in range(1, 4):
        print(f"Lauf {lauf}: ", end="")
        idempotenter_lauf(LOG_DATEI, stichtag=heute)

    print("\n=== Inhalt der Logdatei nach 3 Läufen ===")
    print(LOG_DATEI.read_text(encoding="utf-8").strip())

    # Aufräumen der temporären Demo-Datei
    LOG_DATEI.unlink()


if __name__ == "__main__":
    main()

