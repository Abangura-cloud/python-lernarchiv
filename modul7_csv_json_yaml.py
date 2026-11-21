"""
Modul 7 – Referenz: Strukturierte Datenformate (CSV, JSON & YAML)
"""

import csv
import json
from pathlib import Path
import yaml

PERSONEN = [
    {"name": "Änna", "alter": 34, "ort": "Leipzig"},
    {"name": "Ben", "alter": 28, "ort": "Graz"},
    {"name": "Clara", "alter": 41, "ort": "Basel"},
]

BASIS_PFAD = Path(__file__).parent / "personen_referenz"


def csv_beispiel() -> None:
    """Flache Tabellen: CSV kennt keine Typen (alle Werte werden als str gelesen)."""
    csv_pfad = BASIS_PFAD.with_suffix(".csv")
    with csv_pfad.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "alter", "ort"])
        writer.writeheader()
        writer.writerows(PERSONEN)

    print("--- 1. CSV ---")
    with csv_pfad.open("r", encoding="utf-8", newline="") as f:
        for zeile in csv.DictReader(f):
            alter_int = int(zeile["alter"])
            print(f"{zeile['name']} ({zeile['ort']}): Alter + 1 = {alter_int + 1}")


def json_beispiel() -> None:
    """Verschachtelte Daten & Datentypen (int, float, bool, list, dict) bleiben erhalten."""
    json_pfad = BASIS_PFAD.with_suffix(".json")
    with json_pfad.open("w", encoding="utf-8") as f:
        json.dump(PERSONEN, f, ensure_ascii=False, indent=2)

    print("\n--- 2. JSON ---")
    with json_pfad.open("r", encoding="utf-8") as f:
        geladen = json.load(f)
    print(f"{geladen[0]['name']} ({geladen[0]['ort']}): Alter + 1 = {geladen[0]['alter'] + 1}")


def yaml_beispiel() -> None:
    """Menschenlesbare Konfigurationen (unterstützt # Kommentare; immer safe_load nutzen!)."""
    yaml_pfad = BASIS_PFAD.with_suffix(".yaml")
    with yaml_pfad.open("w", encoding="utf-8") as f:
        yaml.safe_dump(PERSONEN, f, allow_unicode=True, sort_keys=False)

    print("\n--- 3. YAML ---")
    with yaml_pfad.open("r", encoding="utf-8") as f:
        geladen = yaml.safe_load(f)
    for person in geladen:
        print(f"{person['name']} | Alter: {person['alter']} ({type(person['alter']).__name__}) | {person['ort']}")


def main() -> None:
    csv_beispiel()
    json_beispiel()
    yaml_beispiel()


if __name__ == "__main__":
    main()
 
