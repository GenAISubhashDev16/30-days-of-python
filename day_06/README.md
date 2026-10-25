# Day 06: Tuples

## 📖 What I Learned
- Creating tuples, including the one-item tuple `("x",)`
- Tuples are **immutable** (cannot be changed after creation)
- Indexing, slicing, and negative indexes
- Methods: `count()` and `index()`
- Joining tuples with `+` and repeating with `*`
- Converting between tuples and lists to "modify" a tuple
- Unpacking, including `*rest`, and swapping variables
- Using tuples as dictionary keys
- Storing fixed config values and (question, answer) pairs (GenAI use case)

## 📁 Files
| File | Description |
|------|-------------|
| `main.py` | Examples of tuple creation, unpacking, and GenAI patterns |
| `exercises.py` | Solutions to Day 6 exercises (Levels 1-3) |

## ▶️ Run
```bash
uv run main.py
uv run exercises.py
```

## 💡 Key Takeaways
- Use a tuple when the data should **not** change.
- A single-item tuple needs a trailing comma: `("a",)`.
- Tuples have only two methods: `count()` and `index()`.
- `sorted(tuple)` returns a **list**, not a tuple.
- A list inside a tuple can still be changed.