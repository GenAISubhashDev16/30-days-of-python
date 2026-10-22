"""
What is a list?

A list is an ordered, changeable (mutable) collection that can hold any data types. It uses square brackets []

skills=["Python","SQL","LLMs"]
empty=[]

skills[0] #'Python'
skills[-1] #'LLMs'
skills[0:2] #['Python',"SQL"]
skills[::-1] #reversed copy
skills[1]=""PostgreSQL

Method / Function 	What it does
len(lst)	         number of items
count(x)	         how many times x appears
index(x)	         position of x (error if missing)
sort()	             sort in place
sorted(lst)	         return a new sorted list
reverse()	         reverse in place
copy()	             make a shallow copy
min(), max(), sum()	 work on number lists
x in lst	         membership check
"""
# Day 05: Lists

## 📖 What I Learned
- Creating lists and storing mixed data types
- Indexing, slicing, and negative indexes
- Modifying items in place (lists are mutable)
- Adding items: `append`, `insert`, `extend`, `+`
- Removing items: `remove`, `pop`, `del`, `clear`
- Searching and counting: `index`, `count`, `in`
- Sorting: `sort()`, `sorted()`, `reverse()`
- Math functions: `min`, `max`, `sum`, `len`
- Copying lists safely with `copy()`
- Unpacking and nested lists
- Handling chat messages and text chunks as lists (GenAI use case)

## 📁 Files
| File | Description |
|------|-------------|
| `main.py` | Examples of list creation, methods, copying, and GenAI patterns |
| `exercises.py` | Solutions to Day 5 exercises (Levels 1-3) |

## ▶️ Run
```bash
uv run main.py
uv run exercises.py
```

## 💡 Key Takeaways
- Lists are **mutable**: you can change them after creation.
- `b = a` does not copy a list; use `a.copy()`.
- `sort()` changes the list in place, `sorted()` returns a new one.
- `append()` adds one item, `extend()` adds many.
- `pop()` returns the removed item, `remove()` does not.