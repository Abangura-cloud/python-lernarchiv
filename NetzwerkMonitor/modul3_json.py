import json

config_datei = "server_config.json"

server_daten = {
    "standort": "Magdeburg",
    "warnung_ab_ms": 100,
    "server": [
        {"host": "github.com", "ms": 30.0},
        {"host": "python.org", "ms": 46.8},
        {"host": "wikipedia.org", "ms": 69.3}
    ]
}

# Step 1: Save 'server_daten' into 'server_config.json'
with open(config_datei, mode="w", encoding="utf-8") as datei:
    json.dump(server_daten, datei, indent=4)

# Step 2: Load 'server_config.json' safely with full error handling
try:
    with open(config_datei, mode="r", encoding="utf-8") as datei:
        geladene_daten = json.load(datei)
except FileNotFoundError:
    print(f"Fehler: '{config_datei}' existiert nicht!")
except json.JSONDecodeError:
    print(f"Fehler: '{config_datei}' enthält ungültiges JSON!")
else:
    print(f"Konfiguration für Standort '{geladene_daten['standort']}' erfolgreich geladen!")
    for s in geladene_daten["server"]:
        print(f"  - {s['host']}: {s['ms']} ms")
finally:
    print("Datei-Prüfung abgeschlossen.")


