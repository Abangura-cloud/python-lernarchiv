"""
Modul 7 – Referenz: Encodings, Dateimodi (Text vs. Binär) & Robustes Lesen
"""

from pathlib import Path

BEISPIEL_DATEI = Path(__file__).parent / "sonderzeichen_referenz.txt"


def datei_robust_lesen(pfad: Path, encoding: str = "utf-8") -> str:
    """Liest eine Textdatei sicher ein und fängt UnicodeDecodeError ab."""
    pfad = Path(pfad)
    try:
        with pfad.open(mode="r", encoding=encoding) as datei:
            return datei.read()
    except UnicodeDecodeError:
        warnung = (
            f"WARNUNG: '{pfad.name}' konnte nicht strikt mit '{encoding}' "
            "dekodiert werden (Fallback: errors='replace')."
        )
        with pfad.open(mode="r", encoding=encoding, errors="replace") as datei:
            return f"{warnung}\n{datei.read()}"


def main() -> None:
    # 1. Datei explizit in UTF-8 schreiben
    text = "Grüße aus Magdeburg & München — Straße, Größe, Fußball."
    BEISPIEL_DATEI.write_text(text, encoding="utf-8")

    # 2. Encoding-Mismatch demonstrieren
    print("--- 1. Encoding-Mismatch ---")
    print("Latin-1 (stillschweigend verstümmelt):", BEISPIEL_DATEI.read_text(encoding="latin-1"))

    try:
        BEISPIEL_DATEI.read_text(encoding="ascii")
    except UnicodeDecodeError as fehler:
        print("ASCII (UnicodeDecodeError):", fehler)

    print("UTF-8 (korrekt):", BEISPIEL_DATEI.read_text(encoding="utf-8"))

    # 3. Textmodus (str) vs. Binärmodus (bytes)
    print("\n--- 2. Textmodus vs. Binärmodus ---")
    text_inhalt = BEISPIEL_DATEI.read_text(encoding="utf-8")
    binaer_inhalt = BEISPIEL_DATEI.read_bytes()
    print(f"Text ({type(text_inhalt).__name__}): {text_inhalt}")
    print(f"Binär ({type(binaer_inhalt).__name__}): {binaer_inhalt}")

    # 4. Robustes Lesen testen
    print("\n--- 3. Robustes Lesen ---")
    print("Gültig (utf-8):", datei_robust_lesen(BEISPIEL_DATEI, encoding="utf-8"))
    print("Ungültig (ascii):\n", datei_robust_lesen(BEISPIEL_DATEI, encoding="ascii"))


if __name__ == "__main__":
    main()
 
