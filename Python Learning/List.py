# Creating a list
fruits = ["apple", "banana", "cherry", "date"]

# Accessing elements of a list
print("First fruit:", fruits[0])  # Indexing starts from 0
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])  # Negative indexing starts from the end

# Slicing a list
print("Sliced fruits:", fruits[1:3])  # Slicing returns a new list

# Modifying elements of a list
fruits[1] = "blueberry"
print("Modified fruits:", fruits)

# Adding elements to a list
fruits.append("elderberry")
print("After adding a fruit:", fruits)

# Removing elements from a list
removed_fruit = fruits.pop(2)  # Removes and returns the item at the given index
print("Removed fruit:", removed_fruit)
print("Fruits after removal:", fruits)

# Iterating over a list
print("Iterating over fruits:")
for fruit in fruits:
    print(fruit)


characters = [1,2,3,4,5,6,7,8,9]

# List Methods 
characters.sort()    # sorts the list in the ascending order
print(characters)

characters.append(10)   # adds 10 at the end of the lsit 
print(characters)

characters.remove(9)    # removes the selected element
print(characters)    

characters.insert(4,7)   # inserts the entered element at specified index
print(characters)

print(characters.count(7))  # counts the numebr of character

print(characters.pop(9))   #  Removes and returns the item at the specified index. If no index is specified, removes and returns the last item

characters.reverse()    # reverses the  list characters
print(characters)     