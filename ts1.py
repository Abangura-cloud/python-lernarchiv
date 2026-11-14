def a(x):
    if x > 0:
        return "positiv"
print('a is: ', a(1));     # Error

def b(x):
    if x > 0:
        return "positiv"
    return "nicht positiv"

print('b is: ', b(0));     # Correct

def beschreibe(wert):
    match wert:
        case 0:
            return "null"
        case n if n > 0:
            return "positiv"
        case _:
            return "negativ oder unbekannt"

print('Wert ist: ', beschreibe(-7))