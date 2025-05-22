"""
A dictionary is an unordered collection of items
Each item in a dictionary is a key-value pair
Values in a dictionary can be of any data type and mutable
Dictionaries are created using curly braces {}
"""

# Dictionary intro
student = {"name": "John","age": 20,"major": "Computer Science"}


# Accessing dictionary elements
print("\nAccessing dictionary elements:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])


# Modifying dictionary elements
print("\nModifying dictionary elements:")
student["age"] = 21
student["name"] = 'garry'
print("Modified age:", student["age"])
print("Modified name:", student["name"])


# Adding new key-value pairs
print("\nAdding new key-value pairs:")
student["GPA"] = 3.8
print("Updated dictionary:", student)


# Removing key-value pairs
print("\nRemoving key-value pairs:")
del student["major"]
print("Dictionary after removing 'grades' key:", student)



# Methods associated with dictionaries

# Example dictionary
student = {"name": "John","age": 20,"major": "Computer Science","courses": ["Python", "Algorithms", "Database"],"grades": {"Python": 90, "Algorithms": 85, "Database": 88}}

print("\n\nOriginal Dictionary:")
print(student)


# Method: keys()
print("\nKeys in the dictionary:")
print(student.keys())


# Method: values()
print("\nValues in the dictionary:")
print(student.values())


# Method: items()
print("\nKey-Value pairs in the dictionary:")
print(student.items())


# Method: get()
print("\nGet value for key 'name':")
print(student.get("name"))


# Method: pop()
print("\nPop 'age' from the dictionary:")
age = student.pop("age")
print("Popped age:", age)
print("Dictionary after popping 'age':")
print(student)


# Method: update()
print("\nUpdate dictionary with new key-value pairs:")
student.update({"GPA": 3.8, "graduation_year": 2024})
print("Updated dictionary:")
print(student)


# Method: clear()
print("\nClear the dictionary:")
student.clear()
print("Empty dictionary:")
print(student)