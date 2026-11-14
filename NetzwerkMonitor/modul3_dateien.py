import datetime

log_datei = "netzwerk_log.txt"
messwerte = [
    "github.com: 30.0 ms",
    "python.org: 46.8 ms",
    "wikipedia.org: 69.3 ms",
]

# Step 1: Append ("a") new measurements to 'netzwerk_log.txt' using 'with open'
with open(log_datei, mode="a", encoding="utf-8") as datei:
    zeitstempel = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datei.write(f"--- Scan vom {zeitstempel} ---\n")
    for eintrag in messwerte:
        datei.write(f"{eintrag}\n")

# Step 2: Read ("r") the log file back safely using try / except
print("Lese gespeicherte Log-Datei:\n")
try:
    with open(log_datei, mode="r", encoding="utf-8") as datei:
        print(datei.read())
except FileNotFoundError:
    print(f"Fehler: Die Datei '{log_datei}' wurde nicht gefunden!")
