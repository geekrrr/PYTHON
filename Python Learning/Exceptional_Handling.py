# Handling Specific Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


# Handling Multiple Exceptions
try:
    value = int(input("Enter a number: "))
    c = 10 / value
    print("Result:", c)
except ValueError:
    print("Enter a valid number.")
except ZeroDivisionError:
    print("Can't' divide by zero")


# Handling Any Exception
try:
    x = 10 / 0
except Exception as e:
    print("An error occurred:", e)


# Using Else Block
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result:", x)


# Using Finally Block
try:
    file = open("example.txt", "r")
    # Perform file operations
except FileNotFoundError:
    print("File not found!")
finally:      # Using finallly keyword ,execution of that statement is fixed
    file.close()


# Raising Exceptions
def sqrt(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return x ** 0.5

try:
    result = sqrt(-4)
    print("Square root:", result)
except ValueError as ve:
    print("Error:", ve)


# Using assert Statement
def divide(x, y):
    assert y != 0, "Cannot divide by zero."
    return x / y

try:
    result = divide(10, 0)
    print("Result:", result)
except AssertionError as ae:
    print("Assertion Error:", ae)

