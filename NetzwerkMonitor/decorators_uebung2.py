import functools
import time

def zeit_messen(func):
    """Measures and prints how long the decorated function takes to run."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # TODO 1: Record the start time using time.perf_counter()
        start = time.perf_counter()
        # TODO 2: Call func(*args, **kwargs) and save its return value in 'result'
        result = func(*args, **kwargs)
        # TODO 3: Record the end time using time.perf_counter()
        ende = time.perf_counter()
        # TODO 4: Calculate 'dauer = ende - start' and print it formatted to 4 decimals:
        dauer = ende - start
        print(f"[TIMER] '{func.__name__}' dauerte {dauer:.4f} Sekunden.")
        
        return result
        pass

    return wrapper

@zeit_messen
def langsame_berechnung(n):
    """Simulates a heavy calculation by summing squares."""
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    ergebnis = langsame_berechnung(5_000_000)
    print(f"Ergebnis: {ergebnis}")
