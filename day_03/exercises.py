# day 3: exercises
# ----------------- Level 1----------------
# get user's age and check eligibillty to drive
age=int(input("Enter your age : "))
if age>=18:
    print("You are old enough to drive.")
else:
    print(f"you need {18-age} more years to drive.")   
    
#-----------------------Level 2--------------------
#Compare my age with a friend's age
my_age=25
friend_age=int(input("Enter your friend's age: ")) 
print("I am older than my Friend: ",my_age>friend_age)
print("Age differnce: ",abs(my_age-friend_age))

#Compare two numbers
a=int(input("Enter number one: "))
b=int(input("Enter number two: "))
print(f"{a} is grater than {b}:",a>b)
print(f"{a} equals {b} :",a==b)  


#--------- level 3-------------
#Evaluate these and pridict the output before running

print(3>2)# true
print(3>=2)#true
print(3<2)#false
print(2<3)#true
print(2<=3)#true
print(3==2)#false
print(3!=2)#ture

print(len("mango") == len("avocado"))   # False
print(len("mango") != len("avocado"))   # True
print(len("mango") < len("avocado"))    # True
print(len("milk") != len("meat"))       # False
print(len("milk") == len("meat"))       # True
print(len("tomato") == len("potato"))   # True
print(len("python") > len("dragon"))    # False
 

# Use "and", "or", "not"
print(4 > 3 and 10 > 5)           # True
print(4 > 3 and 10 < 5)           # False
print(4 < 3 and 10 < 5)           # False
print(4 > 3 or 10 > 5)            # True
print(4 > 3 or 10 < 5)            # True
print(4 < 3 or 10 < 5)            # False
print(not 4 > 3)                  # False
print(not True)                   # False
print(not False)                  # True

# Check if "on" is found in both "python" and "dragon"
print("on" in "python" and "on" in "dragon")   # True

# Is there "jargon" in the sentence?
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)       # True

# There is no "on" in both "dragon" and "python"? (should be False)
print(not ("on" in "dragon" and "on" in "python"))

# Length of "python" converted to float and then to str
print(str(float(len("python"))))  # 6.0

# Even or odd check
number = int(input("Enter a number: "))
print("Even" if number % 2 == 0 else "Odd")

# Is the floor division of 7 by 3 equal to int(2.7)?
print(7 // 3 == int(2.7))         # True

# Is the type of "10" equal to the type of 10?
print(type("10") == type(10))     # False

# Is int("9.8") equal to 10? (this raises an error, see the note below)
# print(int("9.8") == 10)
print(int(float("9.8")) == 10)    # False

# Pay calculation
# hours = float(input("Enter hours: "))
# rate = float(input("Enter rate per hour: "))
# print("Your weekly earning is", hours * rate)   
# Pay calculation (safe version)
try:
    hours = float(input("Enter hours (e.g. 7 or 7.5): "))
    rate = float(input("Enter rate per hour: "))
    print("Your weekly earning is", hours * rate)
except ValueError:
    print("Please enter numbers only, like 7 or 7.5 (no colons or letters).")
