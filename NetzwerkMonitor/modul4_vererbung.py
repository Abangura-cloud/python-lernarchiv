from dataclasses import dataclass


@dataclass
class Server:
    host: str
    ip: str
    latenz_ms: float

    def ist_langsam(self, grenzwert_ms: float = 100.0) -> bool:
        return self.latenz_ms > grenzwert_ms

    def status_bericht(self) -> str:
        zustand = "LANGSAM" if self.ist_langsam() else "OK"
        return f"[{zustand:<7}] {self.host:<15} ({self.ip}) -> {self.latenz_ms} ms"


@dataclass
class DatabaseServer(Server):
    datenbank_typ: str

    def status_bericht(self) -> str:
        basis_bericht = super().status_bericht()
        return f"{basis_bericht} | DB: {self.datenbank_typ}"


if __name__ == "__main__":
    web_server = Server("github.com", "140.82.121.4", 30.0)
    db_server = DatabaseServer("db-magdeburg-01", "10.0.0.50", 145.2, "PostgreSQL")

    for geraet in [web_server, db_server]:
        print(geraet.status_bericht())
