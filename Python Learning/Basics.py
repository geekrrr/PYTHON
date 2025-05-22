# Integer dataype #
a = 7
b = 98
print(a,b)  # Output: 7 98


# Float datatype #
c = 3.14
d = 7.195
print(c,d)  # Output: 3.14 7.195


# String datatype : We can use both " " and ' ' . Totally choice of personal preference #
name = "ROHIT"
age = '18'
print(name,age)  # Output: ROHIT 18


# Boolean datatype : True means expression is true or correct and False means it not correct #
e = True
f = False
print(7>4)  # Output: True
print(7<4)  # Output: False


# List datatype : It is used to store multiple items in single variable #
Fruits = ['apple','banana','mango','Watermelon']
Numbers = [2,4,6,8,10]
print(Fruits)  # Output: ['apple', 'banana', 'mango', 'Watermelon']
print(Numbers)  # Output: [2, 4, 6, 8, 10]          


# Tuple datatype : It is same as list but the point of difference is tuple is immutable(cannot be changed after creation) #
Nums = (1,2,3,4,5,6)
veggies = ("carrot","raddish","spinach")
print(Nums)  # Output: (1, 2, 3, 4, 5, 6)
print(veggies)  # Output: ('carrot', 'raddish', 'spinach')


# Set datatype : It is a collection of distinct and unique elements #
Table_2 = {2,4,6,8,10,12}
Table_7 = {7,14,21,28}
print(Table_2)  # Output: {2,4,6,8,10,12}


# Dictionary dataype : It is used to store items with a key value for each item used to access there items #
My_dict = {'Name':'Rohit', 'Age':18}
print(My_dict['Name'])  # Output: Rohit
print(My_dict['Age'])   # output: 18


# Input function: Used to take input from user #
name = input("Enter your name: ")
print(name)


# Type function: Used to recognize the type of data stored in the variable #
z = 9
y = 3.14
print(type(z))   # Output: <class 'int'> #
print(type(y))   # Output: <class 'float'> #