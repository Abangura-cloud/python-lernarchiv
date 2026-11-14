import functools

def wiederhole(anzahl):
    """Layer 1 (Factory): Accepts the number of repetitions."""
    def decorator(func):
        """Layer 2 (Decorator): Accepts the function to decorate."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Layer 3 (Wrapper): Runs func 'anzahl' times and returns the last result."""
            result = None
            for _ in range(anzahl):
                result = func(*args, **kwargs)
            return result
            
        return wrapper
    return decorator

@wiederhole(anzahl=3)
def status_pruefen(server_name):
    print(f"Pinge Server '{server_name}'... OK!")
    return f"{server_name}: online"

if __name__ == "__main__":
    endergebnis = status_pruefen("Router-Magdeburg-01")
    print(f"Rückgabewert: {endergebnis}")
