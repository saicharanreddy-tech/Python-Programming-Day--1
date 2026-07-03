"""Write a Python program that:

Takes the user's name (str).
Takes the user's age (int).
Takes the user's percentage (float).
Takes whether they know Python (True/False) and converts it to a Boolean.
Prints all values with their corresponding data types. """

name = input("Enter your name: ")
age = int(input("Enter your age: "))
percentage = float(input("Enter your percentage: "))
knows_python_input = input("Do you know Python? (yes/no): ")
knows_python = knows_python_input.lower() == 'yes'

print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Percentage:", percentage, "Type:", type(percentage))
print("Knows Python:", knows_python, "Type:", type(knows_python))