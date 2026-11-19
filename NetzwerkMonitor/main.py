import json
from pathlib import Path
from models import Server, DatabaseServer
from scanner import misst_zeit, pruefe_server_live
from storage import schreibe_log, speichere_json

STANDARD_HOSTS = ["google.com", "github.com", "python.org", "wikipedia.org"]


def lade_ziel_hosts(dateiname: str = "hosts_config.json") -> list[str]:
    """Loads target hosts from a JSON config file, falling back to STANDARD_HOSTS."""
    pfad = Path(__file__).parent / dateiname if not Path(dateiname).is_absolute() else Path(dateiname)
    if not pfad.exists():
        return STANDARD_HOSTS
    try:
        daten = json.loads(pfad.read_text(encoding="utf-8"))
        hosts = daten.get("hosts", [])
        return hosts if isinstance(hosts, list) and hosts else STANDARD_HOSTS
    except (json.JSONDecodeError, OSError):
        return STANDARD_HOSTS


@misst_zeit(label="Komplett-Monitor")
def starte_monitoring(hosts: list[str]) -> None:
    print("Starte Modularen Netzwerk-Monitor...\n")
    gescannte_server: list[Server] = []

    # 1. Live scan via Generator (yields Server objects)
    for server in pruefe_server_live(hosts):
        print(" ", server.status_bericht())
        gescannte_server.append(server)

    # 2. Add a local DatabaseServer instance (demonstrating Inheritance!)
    lokale_db = DatabaseServer(host="db-magdeburg-01", latenz_ms=12.4, online=True, datenbank_typ="PostgreSQL")
    print(" ", lokale_db.status_bericht())
    gescannte_server.append(lokale_db)

    print()
    schreibe_log(gescannte_server)
    speichere_json(gescannte_server)


if __name__ == "__main__":
    ziel_hosts = lade_ziel_hosts()
    starte_monitoring(ziel_hosts)
