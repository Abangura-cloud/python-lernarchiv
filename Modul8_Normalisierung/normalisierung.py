"""
Normalisierung einer Messreihe: von jedem Wert wird der Mittelwert
der gesamten Reihe abgezogen.

Implementiere hier zwei funktionsgleiche Varianten: einmal mit einer
klassischen Python-Schleife, einmal vektorisiert mit NumPy.
"""

import numpy as np


def normalisiere_schleife(werte: list[float]) -> list[float]:
    """Normalisiert eine Liste von Werten mit einer klassischen Schleife.

    Berechnet den Mittelwert von `werte` selbst (ohne NumPy-Funktion)
    und baut über eine List Comprehension eine neue Liste mit den
    normalisierten Werten auf.
    """
    if not werte:
        return []
    mittelwert = sum(werte) / len(werte)
    return [wert - mittelwert for wert in werte]


def normalisiere_array(werte: np.ndarray) -> np.ndarray:
    """Normalisiert ein NumPy-Array vektorisiert.

    Nutzt `werte.mean()` und Broadcasting, ganz ohne Schleife.
    """
    if werte.size == 0:
        return werte.copy()
    return werte - werte.mean()


if __name__ == "__main__":
    kleine_reihe = [12.5, 9.0, 15.3, 10.1, 13.7]
    kleines_array = np.array(kleine_reihe, dtype=np.float64)

    ergebnis_schleife = normalisiere_schleife(kleine_reihe)
    ergebnis_array = normalisiere_array(kleines_array)

    print("Schleife:", [round(x, 4) for x in ergebnis_schleife])
    print("Array:   ", np.round(ergebnis_array, 4))
    print("Identisch (np.allclose):", np.allclose(ergebnis_schleife, ergebnis_array))
