import functools
import socket
import time
from models import Server


def misst_zeit(label: str):
    """Decorator measuring total execution time of a function."""
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


def pruefe_server_live(hosts: list[str]):
    """Generator: Checks each host via TCP Port 443 and yields a Server object."""
    for host in hosts:
        start = time.perf_counter()
        try:
            with socket.create_connection((host, 443), timeout=2.0):
                ms = (time.perf_counter() - start) * 1000
                yield Server(host=host, latenz_ms=round(ms, 1), online=True)
        except Exception:
            yield Server(host=host, latenz_ms=-1.0, online=False)
