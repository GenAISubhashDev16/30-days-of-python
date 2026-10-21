# Day 04: Strings

## 📖 What I Learned
- Creating strings with single, double, and triple quotes
- Escape sequences: `\n`, `\t`, `\\`
- Concatenation (`+`) and repetition (`*`)
- Formatting with f-strings
- Indexing (positive and negative) and slicing `[start:end:step]`
- Strings are immutable
- Methods: `upper`, `lower`, `capitalize`, `title`, `strip`, `replace`, `split`, `join`, `find`, `index`, `count`, `startswith`, `endswith`, `isalpha`, `isdigit`
- Handling prompts as strings (GenAI use case)

## 📁 Files
| File | Description |
|------|-------------|
| `main.py` | Examples of string creation, slicing, and methods |
| `exercises.py` | Solutions to Day 4 exercises (Levels 1-3) |

## ▶️ Run
```bash
uv run main.py
uv run exercises.py
```

## 💡 Key Takeaways
- Indexing starts at 0; negative indexes count from the end.
- Slicing excludes the end index: `word[0:3]` gives 3 characters.
- Strings cannot be changed in place, methods return a **new** string.
- `find()` returns `-1` when not found; `index()` raises an error.
- `word[::-1]` reverses a string.