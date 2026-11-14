try:
    result = 10 / int(input("Enter a number: "))
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("That wasn't a valid number!")
else:
    print(f"Success! The result is {result}")
finally:
    print("This always runs (like cleaning up database connections).")

