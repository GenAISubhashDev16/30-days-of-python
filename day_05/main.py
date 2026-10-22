# Day 5: Lists

# 1. Creating lists
print("---------------Creating List---------------")
skills=["Python","SQL","LLMs"]
numbers=[5,2,9,1]
maixed=["Subhash",25,True,3.5]
empty=[]
print(skills,numbers,maixed,empty)
print(len(skills))
print(type(skills))



#2 Indexing and slicing
print("---------------------Indexing and slicing-----------")
print(skills[0])#Python
print(skills[-1])#LLms
print(skills[0:2])#['Python','SQL']
print(skills[::-1])#['LLMs','SQL','Python']


#3. Modifying items
print("------------Modifying items-------------")
skills.append("RAG")
skills.insert(1,"FastAPI")
skills.extend(["LangChain","Docker"])
print(skills)
print(["a","b"] + ["c","d"])




# 5. Removing items
print("-----------Removing Items---------------")
skills.remove("Docker")
last=skills.pop() #removes "LangChain"
print("Popped:",last) #remove "Python"

del skills[0]
print(skills)


#6. Counting and searching
print("--------------------Counting and searching------------")
nums=[3,1,3,2,3]
print(nums.count(3)) #3
print(nums.index(2))#3
print(2 in nums) #True
print(10 not in nums) #True

#7. Sorting and reversing
print("------------Sorting and reversing------------")
numbers=[5,2,9,1]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
# numbers(sorted(["b","c","a"]))
# numbers.reverse()
# print(numbers)


#8. math functions on lists
print("----------------math functions lists-------------------")
print(min(numbers),max(numbers),sum(numbers))
print("Average:",sum(numbers)/len(numbers))



#9. Copying (reference vs copy)
print("-----------------Copying reference vs copy")
a=[1,2,3]
b=a
b.append(4)
print("a after b.append:", a) #[1,2,3,4]

c=a.copy()
c.append(5)
print("a after c.append",a) #unchanged
print("c:",c)



# 10. Joining lists
print("---------------joining Lists----------------")
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)

# 11. Unpacking
print("---------------Unpacking------------------------")
first, second, *rest = [10, 20, 30, 40]
print(first, second, rest)

# 12. Nested lists
print("------------------nested List--------------------")
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[1][2])          # 6

# 13. GenAI-style list handling
print("---------------GenAI style list handling-------------------------")
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is RAG?"},
]
messages.append({"role": "assistant", "content": "RAG combines retrieval with generation."})
messages.append({"role": "user", "content": "Give an example."})

print("Total messages:", len(messages))
print("Last message:", messages[-1]["content"])

chunks = ["chunk one", "chunk two", "chunk three"]
context = "\n".join(chunks)
print(context)


