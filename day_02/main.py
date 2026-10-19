# Day 2: variables, Built-in Functions & User Input
# 1. Declearing variables
first_name="Subhash"
last_name="Verma"
role="Gen AI Developer"
age=26
is_learning=True

print(first_name,last_name,role)


#2. Multiple assignment
a,b,c=1,2,3
x=y=z=0

print(a,b,c,x,y,z)


#3. Checking types
print(type(first_name))
print(type(age))
print(type(is_learning))


#4. len()
print(len(first_name))

#5. type casting
num_str='10'
num_int=int(num_str)

num_float=float(num_str)
print(num_int+5) #15
print(num_float+5) #15.0

print(str(100) + "tokens")




# 6. Other built-ins
print(round(3.14159, 2))   # 3.14
print(abs(-7))             # 7
print(max(4, 9, 2))        # 9
print(min(4, 9, 2))        # 2
print(sum([1, 2, 3]))      # 6


# 8. GenAI-style variables
model_name = "gpt-style-model"
temperature = 0.7
max_tokens = 256
prompt = "Explain variables in Python"
print(f"Model: {model_name} | Temp: {temperature} | Max tokens: {max_tokens}")
print(f"Prompt length: {len(prompt)} characters")