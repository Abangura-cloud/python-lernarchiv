import functools
import socket
import time


def misst_zeit(label):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"[{label}] Gesamtdauer: {elapsed:.4f} Sekunden")
            return result
        return wrapper
    return decorator


def pruefe_server_live(hosts):
    """Generator: Connects to real servers on Port 443 and yields live latency."""
    for host in hosts:
        start = time.perf_counter()
        try:
            with socket.create_connection((host, 443), timeout=2.0):
                ms = (time.perf_counter() - start) * 1000
                yield f"  [ONLINE]  {host:<15} -> {ms:.1f} ms"
        except Exception:
            yield f"  [OFFLINE] {host:<15} -> Nicht erreichbar"


@misst_zeit(label="Netzwerk-Scan")
def starte_scan(server_liste):
    print("Starte Live-Abfrage aus Magdeburg...\n")
    for status in pruefe_server_live(server_liste):
        print(status)
    print()


if __name__ == "__main__":
    ziele = ["google.com", "github.com", "python.org", "wikipedia.org"]
    starte_scan(ziele)
