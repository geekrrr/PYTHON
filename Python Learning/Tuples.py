''' Tuples in python
    Definition: 
    A tuple is an immutable sequence in Python, used to store multiple items in a single variable.
    It is defined using curly braces ()
'''


example_tuple = (10, 20, 30, "Python", True)
print("Example Tuple:", example_tuple)


# 2. Accessing Tuple Elements
# Elements in a tuple can be accessed using indices.
print("First Element:", example_tuple[0])
print("Last Element:", example_tuple[-1])


# 3. Tuples are Immutable
# You cannot modify elements in a tuple after its creation.
try:
    example_tuple[1] = 99  # This will raise an error
except TypeError as e:
    print("Error: Tuples are immutable!", e)


# 4. Creating a Tuple with One Element
# A single-element tuple must have a trailing comma.
single_element_tuple = (42,)
print("Single Element Tuple:", single_element_tuple)


# 5. Tuple Packing and Unpacking
# Packing: Assigning multiple values to a tuple
packed_tuple = "Rohit", 25, "Developer"
print("Packed Tuple:", packed_tuple)

# Unpacking: Assigning tuple values to variables
name, age, profession = packed_tuple
print("Unpacked Values: Name:", name, ", Age:", age, ", Profession:", profession)


# 6. Tuple Methods
# Tuples have two main methods: count() and index()
numbers = (1, 2, 3, 2, 5, 2)
print("Count of 2 in Tuple:", numbers.count(2))  # Count occurrences of a value
print("Index of first occurrence of 3:", numbers.index(3))  # Find index of a value


# 7. Iterating through a Tuple
for item in example_tuple:
    print("Iterating Tuple Element:", item)


# 8. Advantages of Tuples
# - Tuples are faster than lists.
# - They can be used as keys in dictionaries (since they are immutable).
# - They are more memory-efficient compared to lists.

# Example of using a tuple as a dictionary key
location = (40.7128, -74.0060)  # Tuple representing coordinates
city_info = {location: "New York City"}
print("City Info Dictionary:", city_info)


# 9. Nesting Tuples
# Tuples can contain other tuples.
nested_tuple = (1, 2, (3, 4), (5, 6))
print("Nested Tuple:", nested_tuple)


# 10. Converting Between Tuples and Other Data Structures
# Convert list to tuple
list_data = [1, 2, 3]
converted_tuple = tuple(list_data)
print("Converted Tuple:", converted_tuple)

# Convert tuple to list
tuple_data = (4, 5, 6)
converted_list = list(tuple_data)
print("Converted List:", converted_list)


# 11. Checking Membership
print("Is 'Python' in example_tuple?", "Python" in example_tuple)