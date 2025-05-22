"""
    Recursion is a programming technique where a function calls itself in order to solve a problem.

    In this factorial function:
      - The base case is when n equals 0, where the factorial of 0 is 1.
      - The recursive case is when n is greater than 0, where the factorial of n is calculated
        by multiplying n with the factorial of (n - 1).
      - The recursion continues until the base case is reached.
 """


def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n - 1)   # Recursive case: n! = n * (n-1)!

# Test the factorial function
number = 5
print(f"The factorial of {number} is:", factorial(number))