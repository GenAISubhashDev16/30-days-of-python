# Day 6: Tuples

# 1. Creating tuples
print("--------------------Creating Tuples--------------------------")
skills = ("Python", "SQL", "LLMs")
numbers = (5, 2, 9, 1)
empty = ()
single = ("Python",)
print(skills, numbers, empty, single)
print(type(skills))
print(type(("Python")))     # str, not tuple
print(len(skills))

# 2. Indexing and slicing
print("----------------------Indexing slicing------------------")
print(skills[0])            # Python
print(skills[-1])           # LLMs
print(skills[0:2])          # ('Python', 'SQL')
print(skills[::-1])         # ('LLMs', 'SQL', 'Python')

# 3. Immutability
# skills[0] = "Java"        # this would raise a TypeError

# 4. Changing a tuple using a list
print("---------------------tuple using list -------------------------------")
temp = list(skills)
temp.append("RAG")
skills = tuple(temp)
print(skills)

# 5. Joining and repeating
print("-------------------------Joining and repeating------------------------")
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)
print(t1 * 3)

# 6. Methods
print("-------------------Methods---------------------")
nums = (3, 1, 3, 2, 3)
print(nums.count(3))        # 3
print(nums.index(2))        # 3

# 7. Built-in functions
print("---------------------------Built-in Functions----------------------")
print(min(nums), max(nums), sum(nums))
print(sorted(nums))         # returns a list
print(3 in nums)            # True

# 8. Unpacking
print("----------------------unpacking---------------------")
name, role = ("Subhash", "Gen AI Developer")
print(name, "-", role)

first, *rest = (1, 2, 3, 4)
print(first, rest)

# 9. Swapping values (uses tuple packing)
print("-----------------------Swapping values--------------------------")
a, b = 1, 2
a, b = b, a
print(a, b)                 # 2 1

# 10. Returning multiple values from a function (preview of Day 11)
print("--------------------Returning multiple value from funcation")
def min_max(values):
    return min(values), max(values)    # returns a tuple

low, high = min_max([4, 8, 1, 9])
print(low, high)

# 11. Tuples as dictionary keys (lists cannot do this)
print("-----------------Tuples as dictionary keys--------------------")
locations = {(28.61, 77.20): "Delhi", (19.07, 72.87): "Mumbai"}
print(locations[(28.61, 77.20)])

# 12. Nested tuples
print("-------------Nested tuples-----------------------")
students = (("Asha", 90), ("Ravi", 85), ("Neha", 92))
print(students[1][0])       # Ravi

# 13. Mutable item inside a tuple (important trap)
print("-------------------Mutable item inside a tuple")
data = ([1, 2], "fixed")
data[0].append(3)           # allowed: the list inside is mutable
print(data)                 # ([1, 2, 3], 'fixed')

# 14. GenAI-style tuples
print("-------------------GenAI-style Tuples--------------")
MODEL_CONFIG = ("gpt-style-model", 0.7, 256)     # name, temperature, max_tokens
model, temperature, max_tokens = MODEL_CONFIG
print(f"Model: {model} | Temp: {temperature} | Max tokens: {max_tokens}")

# (query, answer) pairs for few-shot examples
print("-------------------query answer-----------")
examples = (
    ("2 + 2", "4"),
    ("Capital of India", "New Delhi"),
)
for question, answer in examples:
    print(f"Q: {question} -> A: {answer}")