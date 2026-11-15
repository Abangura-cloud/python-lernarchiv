"""
Modul 6: Live Web APIs & HTTP JSON Requests mit urllib.request und json.
"""

import json
import urllib.request
import urllib.error


def hole_github_profil(benutzername: str) -> dict | None:
    """Fetches public profile data for a GitHub user via the GitHub REST API."""
    url = f"https://github.com{benutzername}"
    anfrage = urllib.request.Request(
        url,
        headers={
            "User-Agent": "LernArchiv-Python-Client/1.0",
            "Accept": "application/vnd.github+json",
        },
    )
    try:
        with urllib.request.urlopen(anfrage, timeout=5.0) as antwort:
            rohtext = antwort.read().decode("utf-8")
            return json.loads(rohtext)
    except urllib.error.HTTPError as fehler:
        print(f"HTTP-Fehler {fehler.code}: {fehler.reason}")
        return None
    except urllib.error.URLError as fehler:
        print(f"Netzwerkfehler: {fehler.reason}")
        return None
    except json.JSONDecodeError:
        print("Fehler: Die Antwort des Servers war kein gültiges JSON.")
        return None


if __name__ == "__main__":
    print("Rufe Live-Daten von der GitHub REST API ab...\n")
    profil = hole_github_profil("Abangura-cloud")

    if profil:
        print(f"GitHub-User:         {profil.get('login')}")
        print(f"Profil-URL:          {profil.get('html_url')}")
        print(f"Öffentliche Repos:   {profil.get('public_repos')}")
        print(f"Erstellt am:         {profil.get('created_at')}")

