# Day 5: Exercises

# ---------- Level 1 ----------
# Declare an empty list
empty_list = []

# List with more than 5 items
items = ["apple", "banana", "mango", "orange", "grapes", "kiwi"]
print(len(items))

# First, middle and last item
first = items[0]
middle = items[len(items) // 2]
last = items[-1]
print(first, middle, last)

# List of your friends / skills
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])

# Change one item
it_companies[0] = "Meta"
print(it_companies)

# Add an item at the end and in the middle
it_companies.append("Anthropic")
it_companies.insert(3, "OpenAI")
print(it_companies)

# Upper case each company
print([company.upper() for company in it_companies])

# Check if "Google" exists
print("Google" in it_companies)

# Sort and reverse
print(sorted(it_companies))
print(sorted(it_companies, reverse=True))

# Slice out first 3 and last 3
print(it_companies[:3])
print(it_companies[-3:])

# Remove first, middle and last
it_companies.pop(0)
it_companies.pop(len(it_companies) // 2)
it_companies.pop()
print(it_companies)

# Clear the list
it_companies.clear()
print(it_companies)

# ---------- Level 2 ----------
frontend = ["HTML", "CSS", "JS", "React", "Redux"]
backend = ["Node", "Express", "MongoDB"]

# Join two lists
full_stack = frontend + backend
print(full_stack)

# Insert "Python" and "SQL" after Redux
index = full_stack.index("Redux")
full_stack.insert(index + 1, "Python")
full_stack.insert(index + 2, "SQL")
print(full_stack)

# Sorting a list of numbers
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = min(ages)
max_age = max(ages)
print(min_age, max_age)

# Add min and max again
ages.append(min_age)
ages.append(max_age)
print(ages)

# Median age
sorted_ages = sorted(ages)
n = len(sorted_ages)
if n % 2 == 1:
    median = sorted_ages[n // 2]
else:
    median = (sorted_ages[n // 2 - 1] + sorted_ages[n // 2]) / 2
print("Median:", median)

# Average age
print("Average:", sum(ages) / len(ages))

# Range
print("Range:", max(ages) - min(ages))

# ---------- Level 3 ----------
# Remove duplicates (set is covered on Day 7)
unique_ages = list(set(ages))
print(sorted(unique_ages))

# Reverse a list without using reverse()
original = [1, 2, 3, 4, 5]
print(original[::-1])

# Count how many times an item appears
fruits = ["apple", "banana", "apple", "mango", "apple"]
print("apple appears", fruits.count("apple"), "times")

# Find the second largest number
nums = [12, 45, 7, 89, 45, 33]
unique_sorted = sorted(set(nums), reverse=True)
print("Second largest:", unique_sorted[1])

# Take user input and build a list
raw = input("Enter numbers separated by commas: ")
user_numbers = [int(x) for x in raw.split(",")]
print("Your list:", user_numbers)
print("Sum:", sum(user_numbers))
print("Max:", max(user_numbers))