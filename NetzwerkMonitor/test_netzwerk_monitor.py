"""
Automatisierte Unit-Tests für NetzwerkMonitor (pytest + unittest.mock).
"""

import json
import socket
from unittest.mock import MagicMock, patch

from models import DatabaseServer, Server
from scanner import pruefe_server_live
from storage import schreibe_log, speichere_json


# --- 1. Tests für models.py ---

def test_server_status_ok_und_langsam():
    schnell = Server(host="python.org", latenz_ms=25.0, online=True)
    langsam = Server(host="://example.com", latenz_ms=150.5, online=True)
    offline = Server(host="://example.com", latenz_ms=-1.0, online=False)

    assert not schnell.ist_langsam()
    assert "[OK     ] python.org" in schnell.status_bericht()

    assert langsam.ist_langsam()
    assert "[LANGSAM] ://example.com" in langsam.status_bericht()

    assert not offline.ist_langsam()
    assert "[OFFLINE] ://example.com" in offline.status_bericht()


def test_database_server_vererbung():
    db = DatabaseServer(host="db-magdeburg-01", latenz_ms=12.4, online=True, datenbank_typ="PostgreSQL")
    assert isinstance(db, Server)
    assert "db-magdeburg-01" in db.status_bericht()
    assert "| DB: PostgreSQL" in db.status_bericht()
    assert db.zu_dict()["datenbank_typ"] == "PostgreSQL"


# --- 2. Tests für scanner.py mit unittest.mock ---

@patch("scanner.socket.create_connection")
def test_pruefe_server_live_erfolg_gemockt(mock_create_connection):
    # Simuliert einen erfolgreichen Context Manager (`with socket.create_connection(...)`)
    mock_conn = MagicMock()
    mock_create_connection.return_value.__enter__.return_value = mock_conn

    ergebnisse = list(pruefe_server_live(["github.com", "python.org"]))

    assert len(ergebnisse) == 2
    assert ergebnisse[0].host == "github.com"
    assert ergebnisse[0].online is True
    assert ergebnisse[0].latenz_ms >= 0.0
    assert mock_create_connection.call_count == 2


@patch("scanner.socket.create_connection", side_effect=socket.timeout("Zeitüberschreitung"))
def test_pruefe_server_live_timeout_gemockt(mock_create_connection):
    ergebnisse = list(pruefe_server_live(["offline-host.local"]))

    assert len(ergebnisse) == 1
    assert ergebnisse[0].host == "offline-host.local"
    assert ergebnisse[0].online is False
    assert ergebnisse[0].latenz_ms == -1.0


# --- 3. Tests für storage.py mit tmp_path ---

def test_schreibe_log_und_speichere_json(tmp_path):
    server_liste = [
        Server(host="github.com", latenz_ms=18.2, online=True),
        DatabaseServer(host="db-magdeburg-01", latenz_ms=5.0, online=True, datenbank_typ="PostgreSQL"),
    ]

    log_datei = tmp_path / "test_log.txt"
    json_datei = tmp_path / "test_report.json"

    schreibe_log(server_liste, dateiname=str(log_datei))
    speichere_json(server_liste, dateiname=str(json_datei))

    log_inhalt = log_datei.read_text(encoding="utf-8")
    assert "github.com" in log_inhalt
    assert "db-magdeburg-01" in log_inhalt

    json_daten = json.loads(json_datei.read_text(encoding="utf-8"))
    assert len(json_daten["ergebnisse"]) == 2
    assert json_daten["ergebnisse"][0]["host"] == "github.com"
    assert json_daten["ergebnisse"][1]["datenbank_typ"] == "PostgreSQL"

