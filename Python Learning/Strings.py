# We can initializee strnigs using three types 
country = 'INDIA'
country = "INDIA"
country = '''INDIA'''


# Slicing of strings 
con1 = country[0:3]  # In country[0:3] , Slicing is done from 0th index upto (3-1)th index #
print(con1)  
con2 = country[0] # Only 0th index element is printed
con3 = country[-5:-1]  # Negative sign is calculated by just subtracting it from length of string . In this case -5 is same as (5-5)th index #
print(con3)


# Slicing using skip 
con4 = country[0:5:2]  # Here in country[0:5:2] , it prints from 0 to 4th index element by skipping to 2nd elements everytime
print(con4)
con5 = country[:5] # if there is nothing before or after ':' then it automatically initializes from 0 and 4th index respectively #


# String Methods
str = 'learning'
print(len(str))   # length of string 
print(str.endswith("ing"))   # checks whether string ends with "ing" or not
print(str.count("n"))   # gives the occurence of "n" in that string
print(str.capitalize())  # captalize first letter of string
print(str.find("t"))   # checks whether "t" is present in the string 
print(str.replace("l","e"))  # replaces the character given in teh string
print(str.upper())  # converts string in upper case
print(str.lower())  # converts  string in the lower case
print(str.title())  # converts enery words's first letter in upper case
print(str.strip())  # Removes leading and trailing whitespace
print(str.lstrip())  # Removes leading whitespace
print(str.rstrip())  # Removes trailing whitespace


# fstring function
firstname = "Tim"
lastname = "David"
print(f"Hi {firstname} {lastname} , welcome to our serives")  # replaces the variable in {} with its value


# Splitting and joining strings
sentence = "This is a sample sentence."
words = sentence.split()  # Split into words
print("Words:", words)


new_sentence = '-'.join(words)  # Join words with hyphen
print("New Sentence:", new_sentence)


# String formatting using % operator
name = "Bob"
age = 25
formatted_string = "My name is %s and I am %d years old." % (name, age)
print("Formatted String:", formatted_string)