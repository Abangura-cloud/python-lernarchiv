"""
Lernmodul 6: Direkter Vergleich — `threading` vs. `asyncio`
============================================================
Key Takeaways:
1. Bei wenigen I/O-Aufgaben (z. B. 5 Quellen) sind `threading` und `asyncio`
   nahezu gleich schnell (~1.01s statt ~5.00s sequenziell).
2. Bei vielen gleichzeitigen Warteoperationen (z. B. 50 oder 500 Quellen)
   skaliert `asyncio` deutlich leichter, weil alle Coroutinen in einer einzigen
   Ereignisschleife (Event Loop) laufen statt eigene OS-Threads anzulegen.
3. `asyncio.gather(*coroutines)` startet und sammelt alle Coroutinen in einer
   einzigen kompakten Anweisung.
"""

import asyncio
import threading
import time


ANZAHL_QUELLEN = 50
WARTEZEIT_SEKUNDEN = 0.5


def hole_daten_thread(quelle_id: int) -> None:
    """Simuliert eine blockierende I/O-Wartezeit in einem eigenen OS-Thread."""
    time.sleep(WARTEZEIT_SEKUNDEN)


def benchmark_threads(anzahl: int) -> float:
    """Führt `anzahl` Warteaufgaben parallel mit `threading.Thread` aus."""
    start = time.perf_counter()
    threads = [
        threading.Thread(target=hole_daten_thread, args=(i,))
        for i in range(1, anzahl + 1)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return time.perf_counter() - start


async def hole_daten_async(quelle_id: int) -> None:
    """Simuliert eine nicht-blockierende I/O-Wartezeit als Coroutine."""
    await asyncio.sleep(WARTEZEIT_SEKUNDEN)


async def benchmark_asyncio(anzahl: int) -> float:
    """Führt `anzahl` Coroutinen gleichzeitig über `asyncio.gather` aus."""
    start = time.perf_counter()
    await asyncio.gather(
        *(hole_daten_async(i) for i in range(1, anzahl + 1))
    )
    return time.perf_counter() - start


if __name__ == "__main__":
    print(f"=== Concurrency-Benchmark ({ANZAHL_QUELLEN} Quellen à {WARTEZEIT_SEKUNDEN}s) ===")
    sequenziell_geschaetzt = ANZAHL_QUELLEN * WARTEZEIT_SEKUNDEN
    print(f"Sequenziell (geschätzt): ~{sequenziell_geschaetzt:.2f} Sekunden")

    dauer_threads = benchmark_threads(ANZAHL_QUELLEN)
    print(f"Threading-Variante:       {dauer_threads:.4f} Sekunden")

    dauer_asyncio = asyncio.run(benchmark_asyncio(ANZAHL_QUELLEN))
    print(f"asyncio-Variante:         {dauer_asyncio:.4f} Sekunden")
 
