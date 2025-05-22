# Open and read a file line by line
with open('sample.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Open a file in write mode and write some text
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")

# Open a file in append mode and add more text
with open('output.txt', 'a') as file:
    file.write("\nAppending this line to the file.")

# Read the entire content of a file into a single string
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)


# Handling Exceptions during File I/O:
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")

import os

# Check if a file exists
if os.path.exists('sample.txt'):
    print("File exists!")

# Get file size
size = os.path.getsize('sample.txt')
print("File size:", size, "bytes")

# Rename a file
os.rename('sample.txt', 'renamed_sample.txt')

# Delete a file
os.remove('renamed_sample.txt')
