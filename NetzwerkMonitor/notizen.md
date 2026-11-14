# Notizen zu Aufgabe 3 und 4

## Aufgabe 3: Ohne functools.wraps

`berechne_summe.__name__` liefert: `"wrapper"`

`berechne_summe.__doc__` liefert: `None`

Begründung: Nach der Dekoration verweist der Name `berechne_summe` nicht mehr auf die ursprüngliche Funktion, sondern auf die vom Decorator zurückgegebene innere Funktion `wrapper`, die selbst keinen Docstring besitzt.

## Aufgabe 4: Mit functools.wraps

`berechne_summe.__name__` liefert: `"berechne_summe"`

`berechne_summe.__doc__` liefert: `"Summiert alle Zahlen von 1 bis n."`

Begründung: `@functools.wraps(func)` kopiert die ursprünglichen Metadaten wie `__name__` und `__doc__` von der Originalfunktion `func` auf die `wrapper`-Funktion, sodass die Identität von `berechne_summe` erhalten bleibt.
