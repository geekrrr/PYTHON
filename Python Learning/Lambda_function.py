"""
A lambda function in Python is a small, anonymous function defined using the lambda keyword. It's also referred to as an anonymous function because it doesn't have a name like a regular function defined with the def keyword.

Lambda functions can have any number of parameters, but they can only contain a single expression. The result of the expression is implicitly returned by the lambda function.
"""
# Lambda expression to add two numbers
add = lambda x, y: x + y

# Lambda expression to square a number
square = lambda x: x ** 2

# Lambda expression to check if a number is even
is_even = lambda x: x % 2 == 0

# Lambda expression to extract the last character of a string
last_character = lambda s: s[-1]

# Example usage of lambda expressions
# Add two numbers using the add lambda expression
print("Addition:", add(3, 5))  # Output: Addition: 8

# Square a number using the square lambda expression
print("Square:", square(4))  # Output: Square: 16

# Check if a number is even using the is_even lambda expression
print("Is even:", is_even(7))  # Output: Is even: False

# Extract the last character of a string using the last_character lambda expression
print("Last character:", last_character("Hello"))  # Output: Last character: o