# Example 1: Defining a simple function without parameters
def greet():
    """This function greets the user."""
    print("Hello, guys!!")

# Example 2: Defining a function with parameters
def add_numbers(x, y):
    """This function adds two numbers and returns the result."""
    result = x + y
    return result

# Example 3: Defining a function with default parameter values
def greet_with_name(name="Anonymous"):
    """This function greets the user with a specified name, or 'Anonymous' if no name is provided."""
    print("Hello,", name)

# Example 4: Defining a function with variable number of arguments
def calculate_sum(*args):
    """This function calculates the sum of all the arguments passed."""
    total = sum(args)
    return total

# Example 5: Defining a function with keyword arguments
def greet_with_title(name, title="Mr."):
    """This function greets the user with a specified title and name."""
    print("Hello,", title, name)

# Example 6: Defining a function with docstring
def area_of_circle(radius):
    """
    This function calculates the area of a circle given its radius.
    Formula: area = π * radius^2
    """
    pi = 3.14159
    area = pi * radius ** 2
    return area
