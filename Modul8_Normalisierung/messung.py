"""
Zeitmessung: vergleiche die Laufzeit von normalisiere_schleife und
normalisiere_array auf kleiner und auf sehr großer Datenmenge.
"""

import time

import numpy as np

from normalisierung import normalisiere_array, normalisiere_schleife


def erzeuge_reihe(anzahl: int) -> tuple[list[float], np.ndarray]:
    """Erzeugt dieselbe Zahlenreihe einmal als Liste, einmal als Array."""
    rng = np.random.default_rng(42)
    arr = rng.random(anzahl, dtype=np.float64)
    return arr.tolist(), arr


def messe_laufzeit(anzahl: int) -> None:
    """Misst und gibt die Laufzeit beider Varianten für `anzahl` Werte aus."""
    werte_liste, werte_array = erzeuge_reihe(anzahl)

    # Bei kleinen Datenmengen mehrfach wiederholen, um Messschwankungen zu glätten
    wiederholungen = 100 if anzahl <= 10_000 else 3

    start_schleife = time.perf_counter()
    for _ in range(wiederholungen):
        normalisiere_schleife(werte_liste)
    dauer_schleife = (time.perf_counter() - start_schleife) / wiederholungen

    start_array = time.perf_counter()
    for _ in range(wiederholungen):
        normalisiere_array(werte_array)
    dauer_array = (time.perf_counter() - start_array) / wiederholungen

    faktor = dauer_schleife / dauer_array if dauer_array > 0 else float("inf")

    print(f"  Schleife (Liste): {dauer_schleife * 1000:.4f} ms")
    print(f"  Array (NumPy):    {dauer_array * 1000:.4f} ms")
    print(f"  Faktor:           NumPy ist {faktor:.1f}x schneller")


if __name__ == "__main__":
    print("Kleine Datenmenge (1.000 Werte):")
    messe_laufzeit(1_000)

    print("\nGroße Datenmenge (10.000.000 Werte):")
    messe_laufzeit(10_000_000)

    # Vergleich der Faktoren (Teilaufgabe 3):
    # Bei einer kleinen Datenmenge (1.000 Werte) ist der Vorsprung von NumPy noch
    # vergleichsweise gering, da der feste Funktionsaufruf- und C-API-Overhead von
    # NumPy im Verhältnis zur kurzen Rechenzeit stärker ins Gewicht fällt.
    # Bei 10.000.000 Werten wächst der Abstand drastisch (oft um Faktor 20x–40x+):
    # Während Python jedes Element einzeln als PyFloatObject in einer interpretierten
    # Schleife verarbeitet, berechnet NumPy die gesamte Operation vektorisiert in
    # zusammenhängendem Speicher (C/SIMD) ohne Interpreter-Overhead.
