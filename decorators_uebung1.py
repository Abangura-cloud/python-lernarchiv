import functools
def log_aufruf(func):
    """A decorator that prints a message before and after a function runs."""
    @functools.wraps(func)
      
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starte Funktion '{func.__name__}'...")
        # TODO 1: Call the original function with *args and **kwargs and save its result
        result = func(*args, **kwargs)
        print(f"[LOG] Funktion '{func.__name__}' beendet.")
        # TODO 2: Return the saved result
        return result
    return wrapper

@log_aufruf
def addiere(a, b):
    return a + b

if __name__ == "__main__":
    ergebnis = addiere(10, 25)
    print(f"Ergebnis: {ergebnis}")

