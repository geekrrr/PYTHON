# Arithmetic operators: +,-,/,*,% #
a = 10
b = 5
print(a+b)   # Addition #
print(a-b)   # Substraction #
print(a/b)   # Division #
print(a*b)   # Multiplication #
print(a%b)   # Modulo operator: Gives remainder #


# Assignment operator: =,+=,-=,*= #
c = a        
print(c)
c += a      # c +=a is simply c = c + b
print(c)
c -= b      # c -=a is simply c = c - b
print(c)
c *= b      # c *=a is simply c = c * b
print(c)


# Comparison operator: ==,<=,>,!= etc #
print(a==b)   # Checks whether a = b or not #
print(a<=b)   # Checks whether a <= b or not #
print(a>b)    # Checks whether a > b or not #
print(a!=b)   # Checks whether a != b or not #


# Logical operator: and , or , not #
print(a>b and a!=b)
print(a>b or a==b)
print(not(a>b))


# Identity operators
a = 5
b = 5
c = [1, 2, 3]
d = [1, 2, 3]

print(a is b)  # True       # is (checks if both variables refer to the same object)
print(c is d)  # False

print(a is not b)  # False    # is not (checks if both variables do not refer to the same object)
print(c is not d)  # True


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