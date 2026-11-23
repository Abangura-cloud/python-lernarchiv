"""
Modul 7 – Referenz: Kommandozeilenprogramme mit argparse & logging
"""

import argparse
import logging

logger = logging.getLogger(__name__)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Definiert CLI-Argumente, erlaubte Werte (choices) und Standardwerte."""
    parser = argparse.ArgumentParser(
        description="Beispiel-CLI für strukturierte Argumente und Logging."
    )
    parser.add_argument(
        "projektname",
        help="Name des auszuwertenden Projekts (Pflichtargument)",
    )
    parser.add_argument(
        "--modus",
        choices=["analyse", "export"],
        default="analyse",
        help="Ausführungsmodus (analyse oder export, Standard: analyse)",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING"],
        default="INFO",
        help="Logging-Stufe (Standard: INFO)",
    )
    return parser.parse_args(argv)


def setup_logging(log_level: str) -> None:
    """Konfiguriert logging über basicConfig (Ausgabe auf stderr)."""
    level = getattr(logging, log_level.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(levelname)s:%(name)s:%(message)s",
        force=True,
    )


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    setup_logging(args.log_level)

    logger.debug("Geparste Argumente: %s", args)
    logger.info("Starte Verarbeitung für '%s' im Modus '%s'...", args.projektname, args.modus)

    # Programmausgabe (stdout) bleibt sauber getrennt von Logging-Meldungen (stderr)
    print(f"Ergebnis: Projekt '{args.projektname}' erfolgreich im Modus '{args.modus}' geprüft.")


if __name__ == "__main__":
    main()

