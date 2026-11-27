"""
Tests für die Normalisierungsfunktionen.
"""

import numpy as np

from normalisierung import normalisiere_array, normalisiere_schleife


def test_normalisiere_schleife_und_array_liefern_gleiches_ergebnis():
    werte_liste = [12.5, 9.0, 15.3, 10.1, 13.7]
    werte_array = np.array(werte_liste)

    ergebnis_schleife = normalisiere_schleife(werte_liste)
    ergebnis_array = normalisiere_array(werte_array)

    assert np.allclose(ergebnis_schleife, ergebnis_array)
    assert np.isclose(sum(ergebnis_schleife), 0.0)


def test_negative_werte():
    werte_liste = [-10.0, -5.0, 0.0, 5.0, 10.0]
    werte_array = np.array(werte_liste)

    ergebnis_schleife = normalisiere_schleife(werte_liste)
    ergebnis_array = normalisiere_array(werte_array)

    assert np.allclose(ergebnis_schleife, [-10.0, -5.0, 0.0, 5.0, 10.0])
    assert np.allclose(ergebnis_schleife, ergebnis_array)


def test_einzelnes_element():
    werte_liste = [42.0]
    werte_array = np.array(werte_liste)

    ergebnis_schleife = normalisiere_schleife(werte_liste)
    ergebnis_array = normalisiere_array(werte_array)

    assert np.allclose(ergebnis_schleife, [0.0])
    assert np.allclose(ergebnis_array, [0.0])
