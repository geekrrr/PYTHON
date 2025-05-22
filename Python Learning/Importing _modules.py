# Importing the math module
import math

# Using functions from the math module
print("Value of pi:", math.pi)  # Output: Value of pi: 3.141592653589793
print("Square root of 16:", math.sqrt(16))  # Output: Square root of 16: 4.0
print("Cosine of pi/3 radians:", math.cos(math.pi/3))  # Output: Cosine of pi/3 radians: 0.5000000000000001



# Importing specific functions from the math module
from math import factorial, radians

# Using the imported functions directly
print("Factorial of 5:", factorial(5))  # Output: Factorial of 5: 120
print("60 degrees in radians:", radians(60))  # Output: 60 degrees in radians: 1.0471975511965976



# Importing all functions/classes from a module (not recommended)
from random import *

# Using functions/classes from the imported module without prefix
random_number = randint(1, 100)
print("Random number between 1 and 100:", random_number)