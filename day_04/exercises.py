# Day 4: Exercises

# ---------- Level 1 ----------
# Concatenate "Thirty", "Days", "Of", "Python" into one string
sentence = "Thirty" + " " + "Days" + " " + "Of" + " " + "Python"
print(sentence)

# Concatenate "Coding", "For", "All" into one string
print("Coding" + " " + "For" + " " + "All")

# Declare a variable named company and assign it a value
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut the first word of the string
print(company[7:])

# Check if "Coding" exists in the string
print(company.index("Coding"))
print(company.find("Coding"))

# Replace "Coding" with "Python"
print(company.replace("Coding", "Python"))

# Change "Python for Everyone" to "Python for All"
print("Python for Everyone".replace("Everyone", "All"))

# Split the string using a space
print(company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split using a comma
tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech.split(", "))

# Character at index 0, last, and index 10
print(company[0])
print(company[-1])
print(company[10])

# Acronym of "Python For Everyone"
print("".join(word[0] for word in "Python For Everyone".split()))

# Index of the first occurrence of "C" in "Coding For All"
print(company.index("C"))

# Index of "F" in "Coding For All"
print(company.index("F"))

# Last occurrence of "l" in "Coding For All"
print(company.rfind("l"))

# ---------- Level 2 ----------
# Does "Coding For All" start with "Coding"?
print(company.startswith("Coding"))

# Does it end with "Coding"?
print(company.endswith("Coding"))

# Trim whitespace
print("   Coding For All      ".strip())

# Check if these are valid variable names (isidentifier)
print("30DaysOfPython".isidentifier())   # False
print("thirty_days_of_python".isidentifier())  # True

# Join a list with a hash
libs = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("# ".join(libs))

# Escape sequences: new line and tab
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\t\tAge\t\tCountry\t\tCity")
print("Asabeneh\t250\t\tFinland\t\tHelsinki")

# Use f-string for the area of a circle
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# ---------- Level 3 ----------
# Personal intro using input and f-strings
name = input("Enter your name: ")
skill = input("Enter your main skill: ")
print(f"Hi, I am {name}. I am learning {skill}.")

# Reverse a string
text = input("Enter a word: ")
print("Reversed:", text[::-1])

# Palindrome check
print("Palindrome:", text == text[::-1])

# Count vowels
vowels = "aeiou"
count = sum(1 for ch in text.lower() if ch in vowels)
print("Vowels:", count)