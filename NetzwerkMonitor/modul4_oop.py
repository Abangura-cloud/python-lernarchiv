from dataclasses import dataclass


@dataclass
class Server:
    """Represents a network server with live latency."""
    host: str
    ip: str
    latenz_ms: float

    def ist_langsam(self, grenzwert_ms: float = 100.0) -> bool:
        """Returns True if latenz_ms is greater than grenzwert_ms."""
        if self.latenz_ms > grenzwert_ms:
            return True
        else:
            return False

    def status_bericht(self) -> str:
        """Returns a formatted status line for this server."""
        zustand = "LANGSAM" if self.ist_langsam() else "OK"
        return f"[{zustand:<7}] {self.host:<15} ({self.ip}) -> {self.latenz_ms} ms"


if __name__ == "__main__":
    # @dataclass automatically creates __init__ and __repr__ for us!
    server_liste = [
        Server("github.com", "140.82.121.4", 30.0),
        Server("google.com", "142.250.185.78", 1281.8),
        Server("python.org", "151.101.0.223", 46.8),
    ]

    print("Automatische __repr__ Ausgabe:")
    print(server_liste[0])

    print("\nStatus-Bericht aller Server:")
    for server in server_liste:
        print(server.status_bericht())
