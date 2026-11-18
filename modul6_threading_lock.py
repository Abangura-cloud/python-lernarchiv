"""
Lernmodul 6: Concurrency mit `threading`, `Lock` & `ThreadPoolExecutor`
========================================================================
Key Takeaways:
1. I/O-bound Aufgaben (Netzwerk-Requests, Wartezeiten) geben den GIL frei -> `threading` beschleunigt sie stark.
2. Greifen mehrere Threads auf denselben veränderlichen Zustand zu, entsteht ohne Schutz eine Race Condition.
3. `threading.Lock()` schützt den gesamten kritischen Abschnitt (`with lock:`), sodass keine Updates verloren gehen.
4. `concurrent.futures.ThreadPoolExecutor` verwaltet Threads elegant per `with`-Statement und sammelt Ergebnisse ein.
"""

from concurrent.futures import ThreadPoolExecutor
import threading
import time


guthaben = 0
lock = threading.Lock()


def einzahlen_sicher(anzahl: int) -> None:
    """Erhöht den globalen Kontostand threadsicher mit `with lock:`."""
    global guthaben
    for _ in range(anzahl):
        with lock:
            guthaben += 1


def pruefe_dienst(name: str) -> str:
    """Simuliert eine I/O-Wartezeit (z. B. Netzwerk-Ping)."""
    time.sleep(0.2)
    return f"{name}: OK (200 ms)"


if __name__ == "__main__":
    print("=== 1. Threadsicheres Hochzählen mit threading.Lock ===")
    threads = [threading.Thread(target=einzahlen_sicher, args=(100_000,)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Erwartet: 400000 | Tatsächlich: {guthaben}\n")

    print("=== 2. Parallele I/O-Checks mit ThreadPoolExecutor ===")
    dienste = ["Auth-API", "Billing-DB", "Storage-Node", "Mail-Relay"]
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        for ergebnis in pool.map(pruefe_dienst, dienste):
            print(" ", ergebnis)
    dauer = time.perf_counter() - start
    print(f"Gesamtdauer für 4 Dienste (parallel): {dauer:.2f}s statt ~0.80s")
 
