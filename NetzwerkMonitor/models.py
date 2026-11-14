from dataclasses import dataclass, asdict


@dataclass
class Server:
    """Represents a monitored network server."""
    host: str
    latenz_ms: float
    online: bool = True

    def ist_langsam(self, grenzwert_ms: float = 100.0) -> bool:
        return self.online and self.latenz_ms > grenzwert_ms

    def status_bericht(self) -> str:
        if not self.online:
            return f"[OFFLINE] {self.host:<15} -> Nicht erreichbar"
        zustand = "LANGSAM" if self.ist_langsam() else "OK"
        return f"[{zustand:<7}] {self.host:<15} -> {self.latenz_ms:.1f} ms"

    def zu_dict(self) -> dict:
        """Converts the object into a dictionary for JSON export."""
        return asdict(self)


@dataclass
class DatabaseServer(Server):
    """Specialized Server subclass for database hosts."""
    datenbank_typ: str = "PostgreSQL"

    def status_bericht(self) -> str:
        return f"{super().status_bericht()} | DB: {self.datenbank_typ}"

