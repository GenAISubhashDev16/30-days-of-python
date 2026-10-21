# day 4: Strings
# 1. creating strings
print("--------Creating string------------")
first_name="Subhash"
last_name='verma'
bio="""Gen AI Developer
Learning Python in 30 days"""

print(first_name,last_name)
print(bio)


#2. escape sequences
print("--------------escape sequences------")
print("Name:\tSubhash")
print("line one\nline two")
print("He said \"Python is great\"")
print("c:\\users\\Subhash")


# 3. Concatenation and repetition
print("------Concatenation and repetiton")
full_name=first_name + " "+ last_name
print(full_name)
print("*" *20)

#4. length
print("------------Length-----------------")

#5. f-strings
role="gen AI Developer"
print(f"{full_name} is a {role}")
price=3.14259
print(f"price: {price:.2f}")


#6. Indexing
print("-------Indexing-------------")
word="Python"
print(word[0]) #p
print(word[-1])#n
print(word[2])#t

#7. slicing
print("------------slicing--------------------")
print(word[0:3])#Pyt
print(word[2:])#thon
print(word[:2])#py
print(word[::2])#pto
print(word[::-1])#nothyp



#8 string methods
print("---------String method------------")
text=" generative AI is amazing "
print(text.strip())
print(text.upper())
print(text.lower())
print(text.strip().capitalize())
print(text.replace("amazing","powerful"))
print(text.count("a"))
print(text.find("AI"))
print(text.strip().startswith("gen"))
print(text.strip().endswith("ing"))



#9. split and join
print("----------------split and join--------------")
skills="Python,sql,llms,RAG"
skill_list=skills.split(",")
print(skill_list)
print(" | ".join(skill_list))


#10. checking content
print("-----------------checking content-------------")
print("abc".isalpha())#true
print("123".isdigit())#true
print("abc123".isalnum())#True


# 11. Immutability
print("------------Immutability---------------")
#word[0]="J" this would raise a typerror
new_word='J'+word[1:]
print(new_word)#Jython


#12. gen ai-style string handling
print("---------------gen ai-style string handling--------------------")
user_prompt="Explain RAG in simple words"
clean_prompt=user_prompt.strip()
print(f"Prompt: {clean_prompt}")
print(f"Characters:{len(clean_prompt)}")
print(f"Words: {len(clean_prompt.split())}")
system_prompt = "You are a helpful assistant."
final_prompt = f"{system_prompt}\nUser: {clean_prompt}"
print(final_prompt)



