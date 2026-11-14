import datetime
import json
from models import Server


def schreibe_log(server_liste: list[Server], dateiname: str = "monitor_log.txt") -> None:
    """Appends a timestamped status report of all servers to a text file."""
    with open(dateiname, mode="a", encoding="utf-8") as datei:
        zeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        datei.write(f"=== Scan vom {zeit} ===\n")
        # TODO 1: Loop through 'server_liste' and write each server.status_bericht() + "\n"
        for server in server_liste:
            server.status_bericht()
            datei.write(f"{server.status_bericht()}\n")

def speichere_json(server_liste: list[Server], dateiname: str = "monitor_report.json") -> None:
    """Exports all Server objects into a structured JSON file."""
    daten = {
        "zeitstempel": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ergebnisse": [s.zu_dict() for s in server_liste]
    }
    try:
        # TODO 2: Open 'dateiname' in mode="w" with encoding="utf-8" as 'datei'
        with open(dateiname, mode="w", encoding="utf-8") as datei:
            json.dump(daten, datei, indent=4)
        
    except OSError as fehler:
        print(f"Fehler beim Speichern von JSON: {fehler}")
    else:
        print(f"JSON-Report erfolgreich in '{dateiname}' gespeichert!")
