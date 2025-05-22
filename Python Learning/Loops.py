"""
1. For Loop: Used for iterating over a sequence (such as a list, tuple, string, etc.) or a range of numbers.
2. While Loop: Used for executing a block of code repeatedly as long as a condition is True.
3. Nested Loops: Used for situations where you need to iterate over multiple sequences or perform repetitive tasks 
   within other tasks, like printing patterns, generating combinations, etc.
4. Input validation: While loops are commonly used for validating user inputs until a valid input is provided.
"""
# Loop Statements in Python

# 1. For Loop:
# Syntax:
# for variable in iterable:
#     # code block to be executed for each iteration

# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: Iterating over a range of numbers
for i in range(1, 5):
    print(i)

# Example 3: Iterating over a string
for char in "Python":
    print(char)

# 2. While Loop:
# Syntax:
# while condition:
#     # code block to be executed as long as the condition is True

# Example 4: Countdown using a while loop
count = 5
while count > 0:
    print(count)
    count -= 1

# 3. Nested Loops:
# Syntax:
# for variable1 in iterable1:
#     for variable2 in iterable2:
#           code block to be executed for each combination of variable1 and variable2

# Example 6: Nested loops to print a multiplication table
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()  # Adding a newline after each table