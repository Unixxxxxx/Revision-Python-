# 🐍 Revision Python 3

> A clean, hands-on Python 3 revision repo covering variables, data types, and the most common beginner mistakes — built to level up your skills fast.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-00d4ff?style=for-the-badge)
![License](https://img.shields.io/badge/License-Open%20Source-7bed9f?style=for-the-badge)

---

## 📁 Files in This Repo

| File | Description |
|------|-------------|
| `variables.py` | Python variable types, assignment, and type conversion |
| `v_common_mistakes.py` | Common beginner mistakes with correct fixes |
| `python.txt` | Quick-reference notes and Python 3 syntax cheatsheet |

---

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/Unixxxxxx/Revision-Python-.git

# 2. Move into the folder
cd Revision-Python-

# 3. Run a file
python3 variables.py
```

---

## 📦 Topic 1 — Variables & Data Types

Python uses **dynamic typing** — you don't need to declare a type, Python figures it out.

```python
# Basic data types
name    = "Unixxxxxx"   # str
age     = 21            # int
height  = 5.9           # float
is_cool = True          # bool

# Multiple assignment in one line
x, y, z = 1, 2, 3

# Check the type
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>

# Type conversion
age_str = str(age)      # int → str: "21"
score   = int("42")     # str → int: 42

# f-strings (Python 3.6+)
print(f"Hello, {name}! You are {age} years old.")
```

### Built-in Types at a Glance

| Type | Example | Notes |
|------|---------|-------|
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `str` | `"hello"` | Text, use quotes |
| `bool` | `True` / `False` | Must be capitalised |
| `list` | `[1, 2, 3]` | Ordered, mutable |
| `tuple` | `(1, 2, 3)` | Ordered, immutable |
| `dict` | `{"key": "val"}` | Key-value pairs |
| `set` | `{1, 2, 3}` | Unique values only |

---

## ⚠️ Topic 2 — Common Mistakes

These are the exact pitfalls covered in `v_common_mistakes.py`.

### ❌ Mistake 1 — `=` vs `==`

```python
# ❌ Wrong — SyntaxError
if x = 5:
    print("five!")

# ✅ Correct — use == for comparison
if x == 5:
    print("five!")
```

> `=` assigns a value. `==` compares two values. Never mix them up.

---

### ❌ Mistake 2 — Concatenating String + Number

```python
age = 20

# ❌ Wrong — TypeError
print("Age: " + age)

# ✅ Correct — convert first
print("Age: " + str(age))

# ✅ Even better — use f-string
print(f"Age: {age}")
```

---

### ❌ Mistake 3 — Mutable Default Argument

```python
# ❌ Wrong — list is shared across ALL calls!
def add_item(item, lst=[]):
    lst.append(item)
    return lst

# ✅ Correct — use None as default
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

> This is one of Python's sneakiest bugs. The default `[]` is created **once** and reused every time.

---

### ❌ Mistake 4 — Off-by-One in `range()`

```python
# ❌ Wrong — prints 0 1 2 3 4 (not 1–5)
for i in range(5):
    print(i)

# ✅ Correct — prints 1 2 3 4 5
for i in range(1, 6):
    print(i)
```

---

### ❌ Mistake 5 — Index Out of Range

```python
my_list = [10, 20, 30]

# ❌ Wrong — IndexError!
print(my_list[3])

# ✅ Correct — last item is index 2, or use -1
print(my_list[2])
print(my_list[-1])   # Pythonic way to get last item
```

---

### ❌ Mistake 6 — Shadowing Built-ins

```python
# ❌ Wrong — overwrites Python's built-in list type!
list = [1, 2, 3]
print(list([4, 5]))  # TypeError

# ✅ Correct — use a descriptive name
my_numbers = [1, 2, 3]
```

> Never name your variables `list`, `str`, `int`, `type`, `input`, etc.

---

## 🗺️ Learning Path

Follow this order to get the most out of the repo:

1. **Read `python.txt`** — warm up with the notes and quick-reference cheatsheet
2. **Run `variables.py`** — observe output, tweak values, experiment with types
3. **Study `v_common_mistakes.py`** — break the code intentionally, read the error, fix it
4. **Extend the repo** — add your own examples and mistake patterns
5. **Repeat** — Python mastery comes from repetition 🔁

---

## 💡 Quick Tips

- Python is **indentation-sensitive** — always use 4 spaces (not tabs)
- Use `print()` and `type()` constantly while learning
- Read error messages carefully — Python's errors are very descriptive
- Write code every day, even just 10 lines

---

## 🔗 Resources

- [Official Python 3 Docs](https://docs.python.org/3/)
- [Python Tutor — Visualise Code](https://pythontutor.com/)
- [Real Python Tutorials](https://realpython.com/)

---

## 👤 Author

**Unixxxxxx** · [GitHub Profile](https://github.com/Unixxxxxx)

---

*Happy coding! 🐍*
