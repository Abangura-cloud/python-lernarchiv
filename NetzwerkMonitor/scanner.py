from concurrent.futures import ThreadPoolExecutor
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


def _pruefe_einzelnen_host(host: str) -> Server:
    """Checks a single host via TCP Port 443 and returns a Server object."""
    start = time.perf_counter()
    try:
        with socket.create_connection((host, 443), timeout=2.0):
            ms = (time.perf_counter() - start) * 1000
            return Server(host=host, latenz_ms=round(ms, 1), online=True)
    except Exception:
        return Server(host=host, latenz_ms=-1.0, online=False)


def pruefe_server_live(hosts: list[str], max_workers: int = 8):
    """Generator: Checks all hosts concurrently via ThreadPoolExecutor and yields Server objects."""
    if not hosts:
        return
    with ThreadPoolExecutor(max_workers=min(max_workers, len(hosts))) as executor:
        for server in executor.map(_pruefe_einzelnen_host, hosts):
            yield server
