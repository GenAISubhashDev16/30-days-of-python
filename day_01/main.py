# Day 1: Introduction to Python

# 1. Printing
print("Hello, World!")
print("Welcome to 30 Days of Python")

# 2. Basic arithmetic
print(2 + 3)    # addition
print(10 - 4)   # subtraction
print(3 * 4)    # multiplication
print(10 / 4)   # division (float result)
print(10 // 4)  # floor division
print(10 % 3)   # remainder
print(2 ** 3)   # power

# 3. Data types
print(type(10))                  # <class 'int'>
print(type(3.14))                # <class 'float'>
print(type(1 + 2j))              # <class 'complex'>
print(type("Python"))            # <class 'str'>
print(type(True))                # <class 'bool'>
print(type([1, 2, 3]))           # <class 'list'>
print(type((1, 2, 3)))           # <class 'tuple'>
print(type({1, 2, 3}))           # <class 'set'>
print(type({"name": "Ravi"}))    # <class 'dict'>

# 4. Indentation example
if 5 > 2:
    print("Five is greater than two")