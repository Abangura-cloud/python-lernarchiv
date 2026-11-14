# The old way (C# style loop)
prices = [10, 20, 30, 40]
Squares = []
for x in prices:
    if x > 15:
        Squares.append(x * x)

Squares = [x * x for x in prices if x > 15]

print(Squares)  # 600, 1000