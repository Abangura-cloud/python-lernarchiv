from models import Server, DatabaseServer
from scanner import misst_zeit, pruefe_server_live
from storage import schreibe_log, speichere_json


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
    # TODO 3: Call 
    schreibe_log(gescannte_server)  
    speichere_json(gescannte_server) 

if __name__ == "__main__":
    ziel_hosts = ["google.com", "github.com", "python.org", "wikipedia.org"]
    starte_monitoring(ziel_hosts)
