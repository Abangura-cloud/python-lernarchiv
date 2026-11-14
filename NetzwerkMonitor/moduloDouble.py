numbers = [1, 2, 3, 4, 5]
squares = []
for x in numbers:
    if x % 2 == 0:
        squares.append(x * x)

# The Python way (List Comprehension)
# Syntax: [expression for item in iterable if condition]
squares = [x * x for x in numbers if x % 2 == 0]

print(squares)  # Outputs: [4, 16]
