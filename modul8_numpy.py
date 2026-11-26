"""
Modul 8: NumPy Grundlagen & Vektorisierung vs. Python-Schleifen.

Demonstriert:
- Erstellung von NumPy-Arrays (np.array, np.arange)
- Vektorisierte Berechnungen (np.sum, elementweise Operationen)
- Geschwindigkeitsvergleich zwischen reiner Python-Schleife und NumPy
"""

import time
import numpy as np


def main() -> None:
    # 1. Basis-Array erstellen und inspizieren
    arr = np.array([1, 2, 3, 4, 5])
    print("Basis-Array:", arr)
    print("Form (shape):", arr.shape, "| Datentyp (dtype):", arr.dtype)
    print("Vektorisiert * 10:", arr * 10)
    print("-" * 50)

    # 2. Geschwindigkeitsvergleich: 1.000.000 Elemente summieren
    anzahl = 1_000_000

    # Variante A: Klassische Python-Liste + for-Schleife
    start_py = time.perf_counter()
    zahlen_py = [float(i) for i in range(anzahl)]
    summe_py = 0.0
    for zahl in zahlen_py:
        summe_py += zahl
    dauer_py = time.perf_counter() - start_py

    # Variante B: Vektorisiertes NumPy-Array + np.sum()
    start_np = time.perf_counter()
    zahlen_np = np.arange(anzahl, dtype=np.float64)
    summe_np = float(np.sum(zahlen_np))
    dauer_np = time.perf_counter() - start_np

    print(f"Python Summe: {summe_py:,.1f} | Dauer: {dauer_py:.5f} s")
    print(f"NumPy Summe:  {summe_np:,.1f} | Dauer: {dauer_np:.5f} s")
    if dauer_np > 0:
        print(f"NumPy war ca. {dauer_py / dauer_np:.1f}x schneller!")


if __name__ == "__main__":
    main()

