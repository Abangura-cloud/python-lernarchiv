# Fallen selbst auslösen und beheben

Willkommen zu dieser Übung aus dem Abschnitt "Der Python-Sprachkern im Schnelldurchlauf".

## Worum geht es

In der letzten Einheit hast du zwei klassische Python-Tücken kennengelernt:

1. Veränderliche Default-Argumente, die sich über mehrere Funktionsaufrufe hinweg "merken"
2. Funktionen, die eine Berechnung durchführen, aber vergessen, das Ergebnis zurückzugeben

In dieser Übung provozierst du beide Fallen selbst im Code, statt sie nur nachzuvollziehen. Am Ende hast du zu jeder Falle eine fehlerhafte und eine korrigierte Fassung geschrieben, beide tatsächlich ausgeführt und ihr unterschiedliches Verhalten beobachtet.

## Aufgaben

### 1. Die Falle mit dem veränderlichen Default-Argument

- Die Funktion `notiere(eintrag, protokoll=[])` ist bereits vorgegeben. Ruf sie dreimal hintereinander auf, jeweils nur mit einem `eintrag` und ohne zweites Argument. Gib nach jedem Aufruf das Ergebnis aus. Beobachte, dass die Liste wächst, statt bei jedem Aufruf neu zu beginnen.
- Schreib die korrigierte Fassung `notiere_korrigiert`, die bei jedem Aufruf ohne zweites Argument mit einem frischen, leeren Protokoll startet. Ruf auch diese Fassung dreimal ohne zweites Argument auf und bestätige durch die Ausgabe, dass jeder Aufruf wieder bei einem Eintrag beginnt.

### 2. Die Falle mit dem fehlenden Return

- Die Funktion `mittelwert(zahlen)` ist bereits vorgegeben, bewusst ohne `return`. Ruf sie mit einer Liste deiner Wahl auf, speichere das Ergebnis in einer Variablen, gib sie aus und gib zusätzlich `type()` dieser Variablen aus.
- Ergänze das fehlende `return` und ruf die Funktion mit derselben Liste erneut auf. Bestätige durch die Ausgabe, dass jetzt der tatsächlich berechnete Mittelwert erscheint.

## Einrichtung und Start

Du brauchst nur eine lokale Python-3-Installation, keine externen Abhängigkeiten.

```bash
python3 fallen.py
```

Bearbeite die Datei `fallen.py`. Alle Stellen, an denen du selbst etwas ergänzen musst, sind mit `# TODO` markiert.

Es gibt keine automatisierten Tests für diese Übung. Überprüfe dein Ergebnis, indem du das Skript ausführst und die Konsolenausgabe mit dem in der Aufgabenstellung beschriebenen Verhalten vergleichst.

