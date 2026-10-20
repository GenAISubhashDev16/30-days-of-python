#day 3: Booloeans & Operators
# 1. Booloeans

is_learning=True
is_finsished=False

print(is_learning,is_finsished)
print(type(is_learning))


# 2. Truthly and falsy values
print("--------------------True and False------------------")
print(bool(0))#False
print(bool(1))#True
print(bool(""))#False
print(bool("Python"))#True
print(bool([]))#False
print(bool([1,2]))#True
#3. Assignment operators
print("----------------------- Assignment operators-------------")
count=10
count+=5#15
count-=3#12
count*=2#24
count/=4#6
count**=2#36.0
print(count)
#4. Arithmetic operators
print("----------Arithmetic operators--------------")
a,b=17,5
print(a+b,a-b,a*b)
print(a/b,a//b,a%b,a**b)

#5. Comparison operators

print("-------------Comparison operators-------------")
print(a==b)#false
print(a!=b)#true
print(a>b)#true
print(a<=b)#false


#6. logical operators
print("---------Logical operators----------------")
age=25
has_skills=True
print(age>18 and has_skills)#True
print(age<18 or has_skills)#True
print(not has_skills) #False

#7. Indetity and membership
print("--------------------Indetity and membership------------")
skills=["Python","SQl","LLMs"]
print("Python" in skills) #true
print("java" not in skills)# true
print("Gen" in "Gen AI Developer")#True

value=None
print(value is None) #true

#8. Chained comparison (Python special)
print("-----------------Chained comparison----------------")
score=75
print(60 <= score <= 100)#True

#9. GenAI-style checks
print("--------------GenAI-style------------------")
temperature=0.7
max_tokens=256
is_valid_temp=0 <= temperature<=2
is_valid_tokens=max_tokens>0 and max_tokens <4096
print("Valid config:",is_valid_temp and is_valid_tokens)
