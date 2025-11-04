"""
Day 2 Practice Exercises - SOLUTIONS
=====================================

This file contains solutions to the practice exercises.
Use this to check answers or as a reference.
"""

print("=" * 60)
print("DAY 2 PRACTICE EXERCISES - SOLUTIONS")
print("=" * 60)
print()

# ============================================================================
# EXERCISE 1: Type Detective - SOLUTIONS
# ============================================================================
print("Exercise 1: Type Detective - SOLUTIONS")
print("-" * 60)

var1 = 42
var2 = "42"
var3 = 3.14
var4 = True
var5 = "True"
var6 = None

print(f"var1 = {var1} → type: {type(var1).__name__}")  # int
print(f"var2 = {var2} → type: {type(var2).__name__}")  # str
print(f"var3 = {var3} → type: {type(var3).__name__}")  # float
print(f"var4 = {var4} → type: {type(var4).__name__}")  # bool
print(f"var5 = {var5} → type: {type(var5).__name__}")  # str
print(f"var6 = {var6} → type: {type(var6).__name__}")  # NoneType
print()

# ============================================================================
# EXERCISE 2: String Operations - SOLUTIONS
# ============================================================================
print("Exercise 2: String Operations - SOLUTIONS")
print("-" * 60)

text = "python programming"

uppercase_text = text.upper()
title_text = text.title()  # Note: .title() capitalizes first letter of each word
position = text.find("prog")
text_length = len(text)

print(f"Original: {text}")
print(f"Uppercase: {uppercase_text}")
print(f"Title case: {title_text}")
print(f"Position of 'prog': {position}")
print(f"Length: {text_length}")
print()

# ============================================================================
# EXERCISE 3: F-strings Practice - SOLUTIONS
# ============================================================================
print("Exercise 3: F-strings Practice - SOLUTIONS")
print("-" * 60)

name = "Sarah"
age = 28
city = "London"
favorite_number = 7

message1 = f"{name} is {age} years old"
message2 = f"{name} lives in {city}"
message3 = f"{name}'s favorite number is {favorite_number}, and next year she'll be {age + 1}"

print(message1)
print(message2)
print(message3)
print()

# ============================================================================
# EXERCISE 4: Type Conversion - SOLUTIONS
# ============================================================================
print("Exercise 4: Type Conversion - SOLUTIONS")
print("-" * 60)

age_str = "25"
price_str = "19.99"
is_active_str = "True"

age = int(age_str)
price = float(price_str)

# Important note: bool("True") and bool("False") both return True!
# To convert string "True"/"False" to boolean, you need to check the string:
is_active = is_active_str.lower() == "true"

print(f"Age: {age} (type: {type(age).__name__})")
print(f"Price: {price} (type: {type(price).__name__})")
print(f"Is active: {is_active} (type: {type(is_active).__name__})")
print()

# ============================================================================
# EXERCISE 5: User Input Challenge - SOLUTIONS
# ============================================================================
print("Exercise 5: User Input Challenge - SOLUTIONS")
print("-" * 60)
print("(Run interactively to see this in action)")
print()

# Uncomment to run:
"""
name = input("What is your name? ")
age_str = input("How old are you? ")
age = int(age_str)
next_year_age = age + 1
print(f"Hello {name}! Next year you'll be {next_year_age} years old.")
"""

# Example output:
print("Example run:")
print("  What is your name? Sarah")
print("  How old are you? 28")
print("  Hello Sarah! Next year you'll be 29 years old.")
print()

# ============================================================================
# EXERCISE 6: Mixed Operations - SOLUTIONS
# ============================================================================
print("Exercise 6: Mixed Operations - SOLUTIONS")
print("-" * 60)
print("(Run interactively to see this in action)")
print()

# Uncomment to run:
"""
num1_str = input("Enter first number: ")
num2_str = input("Enter second number: ")
num1 = int(num1_str)
num2 = int(num2_str)
total = num1 + num2
print(f"{num1} + {num2} = {total}")
"""

# Example output:
print("Example run:")
print("  Enter first number: 5")
print("  Enter second number: 3")
print("  5 + 3 = 8")
print()

# ============================================================================
# EXERCISE 7: If/Else Statements - SOLUTIONS
# ============================================================================
print("Exercise 7: If/Else Statements - SOLUTIONS")
print("-" * 60)

temperature = 25

if temperature >= 25:
    print("It's hot!")
else:
    print("It's cool!")
print()

# ============================================================================
# EXERCISE 8: Elif (Multiple Conditions) - SOLUTIONS
# ============================================================================
print("Exercise 8: Elif (Multiple Conditions) - SOLUTIONS")
print("-" * 60)

score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade F")
print()

# ============================================================================
# EXERCISE 9: While Loops - SOLUTIONS
# ============================================================================
print("Exercise 9: While Loops - SOLUTIONS")
print("-" * 60)

count = 1
while count <= 10:
    print(count)
    count += 1  # Same as count = count + 1
print()

# ============================================================================
# EXERCISE 10: For Loops - SOLUTIONS
# ============================================================================
print("Exercise 10: For Loops - SOLUTIONS")
print("-" * 60)

# Loop over a string
text = "Hello"
for char in text:
    print(char)
print()

# Use range() to print numbers 1 through 5
for i in range(5):
    print(i + 1)  # range(5) gives 0-4, so add 1
print()

# ============================================================================
# EXERCISE 11: Tuples - Basics - SOLUTIONS
# ============================================================================
print("Exercise 11: Tuples - Basics - SOLUTIONS")
print("-" * 60)

colors = ("red", "green", "blue", "yellow", "orange")

print(colors[0])      # First color
print(colors[-1])     # Last color (negative indexing)
print(len(colors))    # Length
print("blue" in colors)  # Membership check
print(colors.index("green"))  # Find index
print()

# ============================================================================
# EXERCISE 12: Tuple Slicing - SOLUTIONS
# ============================================================================
print("Exercise 12: Tuple Slicing - SOLUTIONS")
print("-" * 60)

numbers = (10, 20, 30, 40, 50, 60, 70)

slice1 = numbers[1:3]   # Elements from index 1 to 3 (not including 3)
print(slice1)  # (20, 30)

slice2 = numbers[:3]     # First 3 elements
print(slice2)  # (10, 20, 30)

slice3 = numbers[4:]    # Elements from index 4 to the end
print(slice3)  # (50, 60, 70)
print()

# ============================================================================
# EXERCISE 13: Looping Over Tuples - SOLUTIONS
# ============================================================================
print("Exercise 13: Looping Over Tuples - SOLUTIONS")
print("-" * 60)

fruits = ("apple", "banana", "cherry", "date")

# Option 1: Using range() and indexing
for i in range(len(fruits)):
    print(f"{i + 1}. {fruits[i]}")

print()

# Option 2: Using enumerate() (more Pythonic, but not covered yet)
# for i, fruit in enumerate(fruits, 1):
#     print(f"{i}. {fruit}")

# Simple version (without numbering):
for fruit in fruits:
    print(fruit)
print()

# ============================================================================
# EXERCISE 14: Nested Tuples - SOLUTIONS
# ============================================================================
print("Exercise 14: Nested Tuples - SOLUTIONS")
print("-" * 60)

students = (("Alice", "Bob"), ("Charlie", "Diana"), ("Eve", "Frank"))

print(students[0])        # First inner tuple: ('Alice', 'Bob')
print(students[1][1])      # "Diana" (second element of second tuple)
print()

# ============================================================================
# EXERCISE 15: Combined Challenge - SOLUTIONS
# ============================================================================
print("Exercise 15: Combined Challenge - SOLUTIONS")
print("-" * 60)

numbers = (5, 10, 15, 20, 25)

for num in numbers:
    if num > 10:
        print(f"{num} is greater than 10")
    else:
        print(f"{num} is 10 or less")
print()

print("=" * 60)
print("Solutions complete!")
print("=" * 60)

