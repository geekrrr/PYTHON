""" Sets in Python
   Definition: 
   A set is an unordered collection of unique elements. 
   It is defined using curly braces {}.
"""

# Creating a set
my_set = {1, 2, 3, 4, 5}


# Adding elements to a set
my_set.add(6)
my_set.add(7)


# Removing elements from a set
my_set.remove(3)


# Checking membership in a set
if 4 in my_set:
    print("4 is present in the set\n")
else:
    print("4 is not present in the set\n")


# Set operations
other_set = {4, 5, 6, 8, 9}


# Union of sets
union_set = my_set.union(other_set)
print("Union of sets:", union_set)


# Intersection of sets
intersection_set = my_set.intersection(other_set)
print("\nIntersection of sets:", intersection_set)


# Difference of sets
difference_set = my_set.difference(other_set)
print("\nDifference of sets:", difference_set)


# Checking if a set is a subset of another set
if my_set.issubset(other_set):
    print("\nMy set is a subset of the other set")
else:
    print("\nMy set is not a subset of the other set")
