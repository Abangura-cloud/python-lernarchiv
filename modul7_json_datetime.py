"""
Modul 7 – Referenz: datetime-Objekte in JSON serialisieren und wieder einlesen
"""

from datetime import datetime, timezone
import json
from pathlib import Path

JSON_DATEI = Path(__file__).parent / "ereignisse_referenz.json"


def eigener_json_serializer(obj: object) -> str:
    """Wandelt nicht-JSON-fähige Typen wie datetime sauber in ISO-8601-Strings um."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Typ {type(obj).__name__} ist nicht JSON-serialisierbar")


def main() -> None:
    ereignisse = [
        {
            "titel": "Open-Meteo API-Abfrage",
            "ort": "Magdeburg",
            "zeitstempel": datetime.now(timezone.utc),
        },
        {
            "titel": "CLI-Auswertung mit argparse",
            "ort": "Magdeburg",
            "zeitstempel": datetime(2026, 11, 23, 19, 0, tzinfo=timezone.utc),
        },
    ]

    # 1. Direktes json.dumps ohne default wirft TypeError
    try:
        json.dumps(ereignisse)
    except TypeError as fehler:
        print("1. Ohne default -> TypeError:", fehler)

    # 2. Schnelle Lösung: default=str
    json_mit_str = json.dumps(ereignisse, default=str, ensure_ascii=False, indent=2)
    print("\n2. Mit default=str:\n", json_mit_str)

    # 3. Sauberste Lösung: Eigener ISO-8601-Serializer + Speichern in Datei
    with JSON_DATEI.open("w", encoding="utf-8") as datei:
        json.dump(
            ereignisse,
            datei,
            default=eigener_json_serializer,
            ensure_ascii=False,
            indent=2,
        )

    # 4. Wiedereinlesen und ISO-String zurück in datetime umwandeln
    with JSON_DATEI.open("r", encoding="utf-8") as datei:
        geladene_ereignisse = json.load(datei)

    print("\n3. Wiedergelesen & zurück in datetime konvertiert:")
    for eintrag in geladene_ereignisse:
        dt_objekt = datetime.fromisoformat(eintrag["zeitstempel"])
        print(f"  - {eintrag['titel']}: {dt_objekt!r} (Typ: {type(dt_objekt).__name__})")


if __name__ == "__main__":
    main()

