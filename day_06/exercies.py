"""
A tuple is an ordered,unchangeable(immutable) collection.it users round brackets()
"""

# Day 6: Exercises

# ---------- Level 1 ----------
# Create an empty tuple
print("------------------Empty Tuple---------------")
empty_tuple = ()
print(empty_tuple)

# Tuple of sisters and brothers

sisters = ("Asha", "Neha", "Riya")
brothers = ("Ravi", "Amit")

# Join brothers and sisters
siblings = brothers + sisters
print(siblings)
print(len(siblings))

# Modify siblings into family_members
family_members = list(siblings)
family_members.extend(["Father", "Mother"])
family_members = tuple(family_members)
print(family_members)

# ---------- Level 2 ----------
# Unpack siblings and parents from family_members
*siblings_part, father, mother = family_members
print(siblings_part)
print(father, mother)

# Create fruits, vegetables and animal products tuples
fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("tomato", "potato", "cabbage", "onion", "carrot")
animal_products = ("milk", "meat", "butter", "yoghurt")

# Join into food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Convert to a list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item(s)
n = len(food_stuff_tp)
if n % 2 == 1:
    print(food_stuff_tp[n // 2])
else:
    print(food_stuff_tp[n // 2 - 1 : n // 2 + 1])

# Slice out the first three and last three items
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# Delete the tuple
del food_stuff_tp
# print(food_stuff_tp)   # would raise NameError

# ---------- Level 3 ----------
# Check if an item exists in a tuple
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia" in nordic_countries)   # False
print("Iceland" in nordic_countries)   # True

# Count and index
print(nordic_countries.count("Norway"))
print(nordic_countries.index("Finland"))

# Swap two variables using tuple packing
x, y = 10, 20
x, y = y, x
print(x, y)

# Return min, max and average from a tuple of numbers
scores = (72, 95, 88, 64, 91)
low, high = min(scores), max(scores)
average = sum(scores) / len(scores)
print(f"Min: {low}, Max: {high}, Average: {average}")

# Convert a tuple of tuples to a dictionary preview (full dicts on Day 8)
pairs = (("name", "Subhash"), ("role", "Gen AI Developer"))
print(dict(pairs))

# Take user input and build a tuple
raw = input("Enter numbers separated by commas: ")
user_tuple = tuple(int(x) for x in raw.split(","))
print("Your tuple:", user_tuple)
print("Sorted:", tuple(sorted(user_tuple)))