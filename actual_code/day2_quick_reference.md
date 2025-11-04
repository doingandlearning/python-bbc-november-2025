# Day 2 Morning Review - Quick Reference

## Python Types (Day 1 Recap)

| Type | Example | Description |
|------|---------|-------------|
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `str` | `"Hello"` | Text (in quotes) |
| `bool` | `True`, `False` | Boolean values |
| `NoneType` | `None` | Represents "nothing" |

**Key Point:** Python is **dynamically typed** - variables can change type!

```python
x = 42        # int
x = "hello"   # now it's a str!
```

## Strings

### Concatenation (Old Way)
```python
name = "John" + " " + "Doe"
```

### F-strings (Modern Way - Preferred!)
```python
name = "John"
age = 25
message = f"{name} is {age} years old"
```

### Common String Methods
```python
text = "hello world"
text.upper()        # "HELLO WORLD"
text.lower()        # "hello world"
text.capitalize()   # "Hello world"
text.title()        # "Hello World"
text.find("world")  # 6 (position)
len(text)           # 11 (length)
```

## Type Conversion

```python
# String to number
int("42")      # → 42
float("3.14")  # → 3.14

# Number to string
str(42)        # → "42"
str(3.14)      # → "3.14"

# To boolean
bool(0)        # → False
bool(1)        # → True
bool("")       # → False (empty string)
bool("Hello")  # → True (non-empty)
```

**⚠️ Watch Out:**
- `int("3.14")` → **ERROR!** Can't convert float string directly
- `bool("False")` → **True!** (Any non-empty string is True)
- `input()` always returns a **string** - convert before math!

## User Input

```python
name = input("What's your name? ")  # Returns a string!
age_str = input("How old are you? ")
age = int(age_str)  # Convert to int before math
```

## Common Patterns

### Pattern 1: Get number from user
```python
num_str = input("Enter a number: ")
num = int(num_str)
result = num * 2
print(f"Doubled: {result}")
```

### Pattern 2: String formatting
```python
name = "Alice"
age = 30
print(f"{name} is {age} years old")
```

### Pattern 3: Check type
```python
x = 42
print(type(x))        # <class 'int'>
print(type(x).__name__)  # 'int'
```

## Flow Control

### Comparison Operators
```python
==  # equal to
!=  # not equal to
<   # less than
>   # greater than
<=  # less than or equal
>=  # greater than or equal
```

### If/Else Statements
```python
if condition:
    # do something
else:
    # do something else
```

### Elif (Multiple Conditions)
```python
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade F")
```

### None Testing (Pythonic Way)
```python
if user_name is None:  # Preferred way
    print("Not set")
    
if not user_name:  # Also works
    print("Falsy")
```

### While Loops
```python
count = 1
while count <= 10:
    print(count)
    count += 1  # Same as count = count + 1
```

### For Loops
```python
# Loop over a string
for char in "Hello":
    print(char)

# Loop with range()
for i in range(5):  # 0, 1, 2, 3, 4
    print(i + 1)    # 1, 2, 3, 4, 5
```

### Break Statement
```python
while True:
    if condition:
        break  # Exits loop immediately
```

## Tuples

### Creating Tuples
```python
names = ("Alice", "Bob", "Charlie")  # Immutable (can't be changed)
```

### Indexing (0-based)
```python
names = ("Alice", "Bob", "Charlie")
names[0]   # "Alice" (first element)
names[1]   # "Bob" (second element)
names[-1]  # "Charlie" (last element, negative indexing)
```

### Slicing
```python
numbers = (10, 20, 30, 40, 50)
numbers[1:3]  # (20, 30) - from index 1 to 3 (not including 3)
numbers[:3]   # (10, 20, 30) - from start to index 3
numbers[2:]   # (30, 40, 50) - from index 2 to end
```

### Membership Testing
```python
names = ("Alice", "Bob", "Charlie")
"Bob" in names      # True
"David" in names    # False
```

### Tuple Methods
```python
names = ("Alice", "Bob", "Charlie", "Bob")
len(names)              # 4 (length)
names.count("Bob")      # 2 (count occurrences)
names.index("Bob")      # 1 (find first index)
```

### Looping Over Tuples
```python
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)
```

### Nested Tuples
```python
students = (("Alice", "Bob"), ("Charlie", "Diana"))
students[0]        # ("Alice", "Bob")
students[1][1]     # "Diana"
```

## Quick Tips

1. **Always convert** `input()` to the right type before using it
2. **Use f-strings** for formatting - they're cleaner and easier
3. **Check types** with `type()` if you're unsure
4. **Remember:** Quotes make strings! `"42"` ≠ `42`
5. **Use `is None`** for None testing (Pythonic way)
6. **Tuples are immutable** - you can't change them after creation
7. **Indices start at 0** - first element is `[0]`, not `[1]`
8. **Slicing is exclusive** - `[1:3]` includes 1 but not 3

---

*Good luck with Day 2! 🚀*

