"""
1. Conditional assignment: Assigning values to variables based on conditions.
2. Nested conditions: Using multi-line if-else statements to handle complex conditions.
3. Simplifying if-else statements: Breaking down complex if-else logic into multiple lines for clarity.
4. Traditional control flow: Leveraging the traditional if-else syntax for more extensive conditional logic.
"""

# Defining Conditional Expressions in Python
# result = true_value if condition else false_value


# Example 1: Checking if a number is positive or negative
num = -5
if num >= 0:
    sign = "positive"
else:
    sign = "negative"
print(f"The number {num} is {sign}")


# Example 2: Determining grade based on score
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"The student's grade is {grade}")


# Example 3: Checking if a number is divisible by both 2 and 3
number = 12
if number % 2 == 0 and number % 3 == 0:
    divisible_by_2_and_3 = "Yes"
else:
    divisible_by_2_and_3 = "No"
print(f"The number {number} is divisible by both 2 and 3: {divisible_by_2_and_3}")


# Example 4: Checking if a string is empty or not
string = "Hello"
if not string:
    is_empty = "empty"
else:
    is_empty = "not empty"
print(f"The string is {is_empty}")