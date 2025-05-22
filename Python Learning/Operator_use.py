#ython script to calculate the total cost of painting a room. #

length = int(input("Enter length(in mtr) of room: "))
width = int(input("Enter width(in mtr) of room: "))
height = int(input("Enter the height(in mtr) of room: "))

base_cost = int(input("Give me cost of painting of room per square metre: "))

surface_area = 2*(length*width + width*height + height*length)

cost = base_cost * surface_area

print(cost)



# Program to print the volume of any cylinder providing radius and height #

radius = int(input("Enter the radius of cylinder:"))
Height = int(input("Enter the height of cylinder:"))

volume = 3.14*radius*Height

print(volume)



# Python program to convert temperature from Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32   # Convert Celsius to Fahrenheit using the formula: F = (C * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)



# Python program to calculate the BMI given the weight (in kilograms) and height (in meters) of a person.
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)    # formula: BMI = weight / (height * height)

print("BMI:", bmi)
