# Day 2 Quick Reference - Lists, Dicts, Functions & Classes

## Lists

### Creating Lists
```python
empty_list = []
empty_list = list()
beatles = ["John", "Paul", "George", "Ringo"]
```

**Key Point:** Lists are **mutable** (can be changed) - unlike tuples!

### Indexing & Slicing
```python
beatles = ["John", "Paul", "George", "Ringo"]
beatles[0]      # "John" (first element)
beatles[1]      # "Paul"
beatles[-1]     # "Ringo" (last element)
beatles[1:]     # ["Paul", "George", "Ringo"] (slice)
```

### List Methods

#### Adding Items
```python
beatles = ["John", "Paul", "George", "Ringo"]
beatles.append("Jules")              # Add single item at end
beatles.extend(("Zaid", "Darren"))   # Add multiple items
beatles.insert(0, "Hussain")          # Insert at specific position
```

#### Removing Items
```python
beatles.remove("John")  # Remove first occurrence
# Remove all occurrences:
while "John" in beatles:
    beatles.remove("John")
```

#### Sorting & Reversing
```python
beatles.sort()      # Sort alphabetically (modifies list)
beatles.reverse()   # Reverse order (modifies list)
```

### List Operations
```python
beatles = ["John", "Paul", "George", "Ringo"]
len(beatles)              # 4 (length)
"John" in beatles         # True (membership)
beatles[1] = "New Name"   # Modify element (mutable!)
```

### Nested Lists
```python
bands = [
    ["Freddie Mercury", "Brian May"],  # Queen
    ["Kurt Cobain", "Krist Novoselic"]  # Nirvana
]
bands[0][1]  # "Brian May" (second element of first list)
```

### Looping Over Lists
```python
beatles = ["John", "Paul", "George", "Ringo"]
for member in beatles:
    print(member.upper())
```

---

## Dictionaries

### Creating Dictionaries
```python
empty_dict = {}
user_dict = {
    "name": "Rahul",
    "team": "Product Support",
    "goals": ["Understand Python", "Work with VMs"]
}
```

**Key Point:** Dictionaries store **key-value pairs** - keys must be unique!

### Accessing Values
```python
user_dict = {"name": "Rahul", "team": "Product Support"}
user_dict["name"]           # "Rahul" (direct access)
user_dict.get("name")       # "Rahul" (safe access, returns None if missing)
user_dict.get("age", 0)     # 0 (default value if key missing)
```

### Modifying Dictionaries
```python
user_dict["name"] = "Rahul Soni"          # Update existing key
user_dict["previous_programming"] = []    # Add new key-value pair
```

### Dictionary Methods
```python
user_dict = {"name": "Rahul", "team": "Product Support"}
user_dict.keys()    # dict_keys(['name', 'team'])
user_dict.values()  # dict_values(['Rahul', 'Product Support'])
user_dict.items()   # dict_items([('name', 'Rahul'), ('team', 'Product Support')])
```

### Membership Testing
```python
user_dict = {"name": "Rahul", "team": "Product Support"}
"name" in user_dict      # True (checks KEYS, not values!)
"Rahul" in user_dict     # False (checks keys, not values!)
```

### Looping Over Dictionaries
```python
user_dict = {"name": "Rahul", "team": "Product Support"}

# Loop over keys
for key in user_dict.keys():
    print(key)

# Loop over values
for value in user_dict.values():
    print(value)

# Loop over items (key-value pairs)
for item in user_dict.items():
    print(f"{item[0]} => {item[1]}")

# Or unpack directly:
for key, value in user_dict.items():
    print(f"{key} => {value}")
```

---

## Functions

### Defining Functions
```python
def print_hello():
    print("Hello!")
    print("=" * 20)

print_hello()  # Call the function
```

### Functions with Parameters
```python
def say_hello_to_user(name, separator="=", width=20):
    """
    A function to say hello to a user with separators
    
    Arguments:
        - name: The user's name
        - separator: Character to use (defaults to =)
        - width: Width of separator line (defaults to 20)
    """
    print(separator * width)
    print(f"Hello {name}")
    print(separator * width)

# Different ways to call:
say_hello_to_user("Brodie", width=25)
say_hello_to_user("Andy", "*", 15)
say_hello_to_user(name="Chris", separator="+", width=10)
```

### Parameters & Arguments
- **Positional arguments:** Must be in order
- **Keyword arguments:** Specify by name (can be in any order)
- **Default arguments:** Have default values if not provided

### Returning Values
```python
def add(num1, num2):
    """Adds two numbers together"""
    total = num1 + num2
    return total

result = add(1, 2)  # result = 3
print(result)
```

### Functions that Return Lists
```python
def get_readings_from_user():
    """Return a list of values from a user"""
    readings = []
    while True:
        reading = input("Please enter reading (q to quit): ")
        if reading == "q":
            break
        readings.append(reading)
    return readings

user_readings = get_readings_from_user()
```

**Key Principle:** DRY - Don't Repeat Yourself!

---

## More Functions

### Variable Arguments (*args)
```python
def add(*numbers):  # *args collects all arguments into a tuple
    total = 0
    for n in numbers:
        total += n
    return total

print(add(1, 2))        # 3
print(add(4, 4, 5))     # 13
print(add(5, 4, 4, 5))  # 18
```

**Note:** `*args` allows functions to accept any number of arguments!

### Scope & Global Variables
```python
count = 1  # Global variable

def print_count():
    global count  # Gives write access to global variable
    count = count + 1
    print(f"Count inside: {count}")

print(f"Count outside (before): {count}")
print_count()
print(f"Count outside (after): {count}")
```

### Scope Rules
1. **Functions can read** variables outside themselves
2. **Shadowing:** Local variables take priority over global ones with same name
3. **Variables created inside** functions can't be accessed outside

### List Comprehensions
```python
# Traditional way:
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled_numbers = []
for number in number_list:
    if number < 7:
        doubled_numbers.append(number * 2)

# List comprehension (shorter!):
doubled_numbers = [
    number * 2 
    for number in number_list 
    if number < 7
]

# Another example:
names = ["Brodie", "Siobhan", "Chris"]
upper_names = [name.upper() for name in names]
```

**List Comprehension Syntax:**
```python
[expression for item in iterable if condition]
```

---

## Classes

### What are Classes?
- **Class:** Recipe/blueprint/template (defines structure)
- **Object/Instance:** Actual thing created from the class
- **Attributes/Fields:** Data stored in the object
- **Methods/Behaviors:** Functions that belong to the object

### Creating a Simple Class
```python
class User:
    def __init__(self, name, location, team, role="Unknown"):
        # __init__ is called when creating a new instance
        self.name = name
        self.location = location
        self.team = team
        self.role = role
    
    def __str__(self):
        # Defines how the object is printed
        return f"User(name={self.name}, location={self.location}, team={self.team}, role={self.role})"
    
    def introduce_self(self):
        # Instance method - can access self
        print(f"Hi, I'm {self.name}. I'm a {self.role} in the {self.team} team living in {self.location}.")
    
    def is_weekend(self, day):
        # Instance method with parameter
        match day:
            case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
                return False
            case _:
                return True
```

### Creating Instances (Objects)
```python
# Create instances of the User class
user3 = User(name="Jules", location="Reading", team="BBC Monitoring")
user4 = User("Zaid", "Salford", "Catalogue", "Developer Engineer")

# Access attributes
print(user3.name)  # "Jules"
print(user4.name)  # "Zaid"

# Call methods
user3.introduce_self()
user4.introduce_self()

# Use methods with parameters
print(user3.is_weekend("Monday"))    # False
print(user4.is_weekend("Saturday"))  # True
```

### Special Methods (Dunder Methods)
- `__init__(self, ...)`: Called when creating a new instance
- `__str__(self)`: Defines how the object is printed with `print()`
- `__repr__(self)`: Defines the "official" string representation

**Key Points:**
- `self` is always the first parameter in instance methods
- `self` refers to the specific instance of the class
- Attributes are accessed via `self.attribute_name`
- Methods are defined like functions but inside the class

---

## Quick Tips

### Lists vs Tuples
- **Lists:** Mutable (can change) - use `[]`
- **Tuples:** Immutable (can't change) - use `()`
- Use lists when you need to modify the data
- Use tuples when data shouldn't change

### Dictionary Keys
- Keys must be **unique**
- Keys must be **immutable** (strings, numbers, tuples - NOT lists)
- `in` operator checks **keys**, not values!

### Functions
1. **Use docstrings** (`"""..."""`) to document your functions
2. **Return values** when you need to use the result
3. **Use default arguments** for optional parameters
4. **DRY principle:** Don't Repeat Yourself - use functions!

### Scope
- Variables inside functions are **local** - can't access outside
- Use `global` keyword to modify global variables inside functions
- Local variables **shadow** (hide) global variables with same name

### List Comprehensions
- Use for **simple transformations** and filtering
- More **readable** for simple operations
- Faster than loops for simple cases
- Can be nested for complex operations

### Classes
- Classes are **blueprints** for creating objects
- `__init__` is the **constructor** (runs when object is created)
- `self` refers to the **current instance**
- Methods are **functions** that belong to the class
- Use classes to **organize related data and behavior**

---

*Good luck with Day 3! 🚀*

