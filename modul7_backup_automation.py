#!/usr/bin/env python3
"""
Backup-Skript fuer den unbeaufsichtigten Betrieb.

Notiz zur Befehlswahl und zum Testen:
- Gewaehlter Sicherungsbefehl: `tar -czf <zielarchiv> -C <quell_elternordner> <quell_name>`.
  `tar` ist sowohl unter Windows (ab Windows 10 integriert) als auch unter Linux und macOS
  verfuegbar und erzeugt komprimierte `.tar.gz`-Archive ohne Probleme mit Windows-Laufwerksbuchstaben.
- Getestet wurde:
  1. Erster Lauf mit einem dedizierten Testordner -> Archiv `.tar.gz` wurde erstellt, Exit-Code 0.
  2. Zweiter Lauf am selben Tag -> Sicherung wurde idempotent uebersprungen, kein Duplikat, Exit-Code 0.
  3. Drei gezielt provozierte Fehlerfaelle (nicht existierender Quellordner, nicht gefundener
     Archivierungsbefehl sowie schreibgeschuetztes Zielverzeichnis) -> alle drei wurden mit
     vollstaendigem Traceback in `~/.backup_skript.log` protokolliert und lieferten Exit-Code != 0.

Das Skript sichert einen Quellordner ueber einen externen Archivierungsbefehl
in ein Zielverzeichnis. Es legt pro Tag nur eine Sicherung an, protokolliert
jeden Schritt und beendet sich mit einem aussagekraeftigen Exit-Code.
"""

from __future__ import annotations

import argparse
import logging
import os
import platform
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

STANDARD_LOGDATEI = Path.home() / ".backup_skript.log"


def logger_einrichten(logdatei: Path) -> logging.Logger:
    """Richtet einen Logger ein, der in eine feste Logdatei schreibt."""
    logdatei.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Vorhandene Handler entfernen, damit bei mehrfachem Aufruf keine doppelten Zeilen entstehen
    for handler in list(logger.handlers):
        logger.removeHandler(handler)
        handler.close()

    file_handler = logging.FileHandler(logdatei, mode="a", encoding="utf-8")
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def archivierungsbefehl_waehlen() -> str:
    """Waehlt abhaengig von der Plattform einen verfuegbaren Archivierungsbefehl."""
    system = platform.system()
    if system in ("Windows", "Linux", "Darwin"):
        kandidat = "tar"
    else:
        kandidat = "tar"

    pfad = shutil.which(kandidat)
    if pfad is None:
        raise FileNotFoundError(
            f"Archivierungsbefehl '{kandidat}' wurde auf Plattform '{system}' nicht gefunden."
        )
    return pfad


def sicherungsname_erzeugen(quellordner: Path) -> str:
    """Erzeugt den Dateinamen der heutigen Sicherung."""
    heute = date.today().isoformat()
    bereinigter_name = quellordner.resolve().name or "backup"
    return f"{bereinigter_name}_{heute}.tar.gz"


def sicherung_existiert_bereits(zielverzeichnis: Path, sicherungsname: str) -> bool:
    """Prueft, ob fuer den heutigen Tag bereits eine Sicherung existiert."""
    zielpfad = zielverzeichnis / sicherungsname
    return zielpfad.is_file()


def sicherung_erstellen(
    quellordner: Path, zielverzeichnis: Path, logger: logging.Logger
) -> Path:
    """Sichert quellordner nach zielverzeichnis ueber einen externen Unterprozess."""
    befehl_pfad = archivierungsbefehl_waehlen()
    sicherungsname = sicherungsname_erzeugen(quellordner)
    zielarchiv = zielverzeichnis / sicherungsname

    kommando = [
        befehl_pfad,
        "-czf",
        str(zielarchiv),
        "-C",
        str(quellordner.parent),
        quellordner.name,
    ]

    logger.info("Starte Unterprozess zur Sicherung: %s", kommando)
    ergebnis = subprocess.run(
        kommando,
        capture_output=True,
        text=True,
        check=True,
    )
    logger.info(
        "Unterprozess erfolgreich beendet (Returncode=%s). Archiv: %s",
        ergebnis.returncode,
        zielarchiv,
    )
    return zielarchiv


def _zielverzeichnis_pruefen(zielverzeichnis: Path) -> None:
    """Stellt sicher, dass das Zielverzeichnis existiert und beschreibbar ist."""
    zielverzeichnis.mkdir(parents=True, exist_ok=True)
    if not zielverzeichnis.is_dir():
        raise NotADirectoryError(f"Zielpfad ist kein Verzeichnis: {zielverzeichnis}")

    testdatei = zielverzeichnis / f".schreibtest_{os.getpid()}.tmp"
    try:
        testdatei.write_text("ok", encoding="utf-8")
    finally:
        if testdatei.exists():
            testdatei.unlink()


def hauptprogramm() -> int:
    """Fuehrt den kompletten Ablauf aus und liefert den Exit-Code."""
    args = argumente_parsen()
    quellordner = args.quellordner.expanduser().resolve()
    zielverzeichnis = args.zielverzeichnis.expanduser().resolve()

    logger = logger_einrichten(STANDARD_LOGDATEI)
    logger.info(
        "Backup-Lauf gestartet (Quelle: %s, Ziel: %s)",
        quellordner,
        zielverzeichnis,
    )

    try:
        # Fehlerfall 1: Fehlender oder nicht lesbarer Quellordner
        if not quellordner.exists():
            raise FileNotFoundError(f"Quellordner existiert nicht: {quellordner}")
        if not quellordner.is_dir():
            raise NotADirectoryError(f"Quellpfad ist kein Verzeichnis: {quellordner}")
        if not os.access(quellordner, os.R_OK):
            raise PermissionError(f"Keine Leserechte fuer Quellordner: {quellordner}")

        # Fehlerfall 2: Fehlende Schreibrechte im Zielverzeichnis
        _zielverzeichnis_pruefen(zielverzeichnis)

        # Idempotenz-Pruefung fuer den heutigen Tag
        sicherungsname = sicherungsname_erzeugen(quellordner)
        if sicherung_existiert_bereits(zielverzeichnis, sicherungsname):
            logger.info(
                "Sicherung '%s' existiert heute bereits in '%s' – Vorgang wird uebersprungen.",
                sicherungsname,
                zielverzeichnis,
            )
            logger.info("Backup-Lauf erfolgreich abgeschlossen (Exit-Code 0).")
            return 0

        logger.info("Keine heutige Sicherung vorhanden – erstelle '%s'.", sicherungsname)
        erzeugtes_archiv = sicherung_erstellen(quellordner, zielverzeichnis, logger)
        logger.info("Backup-Lauf erfolgreich abgeschlossen: %s (Exit-Code 0).", erzeugtes_archiv)
        return 0

    except (FileNotFoundError, NotADirectoryError) as fehler:
        logger.exception("Quell- oder Befehlsfehler beim Backup: %s", fehler)
        return 2
    except PermissionError as fehler:
        logger.exception("Fehlende Berechtigungen beim Backup: %s", fehler)
        return 3
    except subprocess.CalledProcessError as fehler:
        logger.exception(
            "Archivierungs-Unterprozess fehlgeschlagen (Returncode %s): %s",
            fehler.returncode,
            fehler.stderr,
        )
        return 4
    except OSError as fehler:
        logger.exception("Betriebssystem-/Dateisystemfehler beim Backup: %s", fehler)
        return 5


def argumente_parsen() -> argparse.Namespace:
    """Liest Quellordner und Zielverzeichnis von der Kommandozeile ein."""
    parser = argparse.ArgumentParser(description="Sichert einen Ordner per externem Archivierungsbefehl.")
    parser.add_argument("quellordner", type=Path, help="Zu sichernder Ordner")
    parser.add_argument("zielverzeichnis", type=Path, help="Verzeichnis fuer die Sicherung")
    return parser.parse_args()


if __name__ == "__main__":
    sys.exit(hauptprogramm())

