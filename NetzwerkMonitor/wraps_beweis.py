import functools

def ohne_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def mit_wraps(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@ohne_wraps
def funktion_a():
    """Ich bin Dokumentation A."""
    pass

@mit_wraps
def funktion_b():
    """Ich bin Dokumentation B."""
    pass

print("Ohne wraps -> Name:", funktion_a.__name__, "| Doc:", funktion_a.__doc__)
print("Mit wraps  -> Name:", funktion_b.__name__, "| Doc:", funktion_b.__doc__)
