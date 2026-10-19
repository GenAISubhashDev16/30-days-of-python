# Day 2: Exercises

# ---------- Level 1 ----------
# Variables
first_name = "Subhash"
last_name = "Verma"
full_name = first_name + " " + last_name
country = "India"
city = "Delhi"
age = 25
year = 2026
is_married = False
is_true = True
is_light_on = False

# Multiple variables in one line
num_one, num_two, num_three = 5, 4, 3

print(full_name, country, city, age, year)
print(is_married, is_true, is_light_on)

# ---------- Level 2 ----------
# Check the type of each variable
print(type(first_name), type(age), type(is_married))

# Length of first and last name
print(len(first_name), len(last_name))
print(len(first_name) > len(last_name))

# Arithmetic with num_one = 5 and num_two = 4
num_one = 5
num_two = 4
print("Sum:", num_one + num_two)
print("Difference:", num_one - num_two)
print("Product:", num_one * num_two)
print("Division:", num_one / num_two)
print("Remainder:", num_one % num_two)
print("Exponent:", num_one ** num_two)
print("Floor division:", num_one // num_two)

# Area and circumference of a circle (radius = 30 meters)
radius = 30
pi = 3.14
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius
print("Area:", area_of_circle)
print("Circumference:", circum_of_circle)

# Radius from user input
radius = float(input("Enter radius: "))
print("Area:", pi * radius ** 2)

# ---------- Level 3 ----------
# Ask the user for personal info and display it
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
country = input("Which country do you live in? ")
age = input("How old are you? ")

print(f"Name: {first_name} {last_name}")
print(f"Country: {country}")
print(f"Age: {age}")

# Bonus: show how Python's keywords/built-ins can be listed
import keyword
print(keyword.kwlist)




"input------------------------------output"
# Subhash Verma India Delhi 25 2026
# False True False
# <class 'str'> <class 'int'> <class 'bool'>
# 7 5
# True
# Sum: 9
# Difference: 1
# Product: 20
# Division: 1.25
# Remainder: 1
# Exponent: 625
# Floor division: 1
# Area: 2826.0
# Circumference: 188.4
# Enter radius: 12
# Area: 452.16
# What is your first name? subhash
# What is your last name? verma
# Which country do you live in? Gurugram
# How old are you? 25
# Name: subhash verma
# Country: Gurugram
# Age: 25
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']