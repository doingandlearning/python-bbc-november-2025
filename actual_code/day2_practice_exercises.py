"""
Day 2 Practice Exercises - Morning Review
==========================================

Work through these exercises to reinforce Day 1 concepts.
"""

print("=" * 60)
print("DAY 2 PRACTICE EXERCISES")
print("=" * 60)
print()

# ============================================================================
# EXERCISE 1: Type Detective
# ============================================================================
print("Exercise 1: Type Detective")
print("-" * 60)
print("Predict the type, then check with type()")
print()

# TODO: Predict the type of each variable, then uncomment the print statements
var1 = 42
var2 = "42"
var3 = 3.14
var4 = True
var5 = "True"
var6 = None

# Uncomment these to check your answers:
# print(f"var1 = {var1} → type: {type(var1).__name__}")
# print(f"var2 = {var2} → type: {type(var2).__name__}")
# print(f"var3 = {var3} → type: {type(var3).__name__}")
# print(f"var4 = {var4} → type: {type(var4).__name__}")
# print(f"var5 = {var5} → type: {type(var5).__name__}")
# print(f"var6 = {var6} → type: {type(var6).__name__}")
print()

# ============================================================================
# EXERCISE 2: String Operations
# ============================================================================
print("Exercise 2: String Operations")
print("-" * 60)
print("Complete these string operations:")
print()

text = "python programming"

# TODO: Create variables with these transformations:
# 1. Convert to uppercase
# uppercase_text = ???

# 2. Convert to title case (first letter of each word capitalized)
# title_text = ???

# 3. Find the position of "prog" in the string
# position = ???

# 4. Get the length of the string
# text_length = ???

# Uncomment to check:
# print(f"Original: {text}")
# print(f"Uppercase: {uppercase_text}")
# print(f"Title case: {title_text}")
# print(f"Position of 'prog': {position}")
# print(f"Length: {text_length}")
print()

# ============================================================================
# EXERCISE 3: F-strings Practice
# ============================================================================
print("Exercise 3: F-strings Practice")
print("-" * 60)
print("Create f-strings for these scenarios:")
print()

name = "Sarah"
age = 28
city = "London"
favorite_number = 7

# TODO: Create these messages using f-strings:
# 1. "Sarah is 28 years old"
# message1 = ???

# 2. "Sarah lives in London"
# message2 = ???

# 3. "Sarah's favorite number is 7, and next year she'll be 29"
# message3 = ???

# Uncomment to check:
# print(message1)
# print(message2)
# print(message3)
print()

# ============================================================================
# EXERCISE 4: Type Conversion
# ============================================================================
print("Exercise 4: Type Conversion")
print("-" * 60)
print("Convert these values correctly:")
print()

# TODO: Convert these strings to the correct types
age_str = "25"
price_str = "19.99"
is_active_str = "True"

# Convert age_str to an integer
# age = ???

# Convert price_str to a float
# price = ???

# Convert is_active_str to a boolean
# Note: bool("True") gives True, but bool("False") also gives True!
# Think about this carefully...

# Uncomment to check:
# print(f"Age: {age} (type: {type(age).__name__})")
# print(f"Price: {price} (type: {type(price).__name__})")
# print(f"Is active: {is_active_str} → ???")
print()

# ============================================================================
# EXERCISE 5: User Input Challenge
# ============================================================================
print("Exercise 5: User Input Challenge")
print("-" * 60)
print("Create a program that:")
print("1. Asks for the user's name")
print("2. Asks for their age")
print("3. Calculates their age next year")
print("4. Prints a personalized message")
print()

# TODO: Uncomment and complete this code:
"""
# Get user's name
name = input(???)

# Get user's age (remember: input() returns a string!)
age_str = input(???)

# Convert age to integer
age = ???

# Calculate next year's age
next_year_age = ???

# Print personalized message using f-string
print(f"Hello {name}! Next year you'll be {next_year_age} years old.")
"""

# ============================================================================
# EXERCISE 6: Mixed Operations
# ============================================================================
print("Exercise 6: Mixed Operations")
print("-" * 60)
print("Combine what you've learned:")
print()

# TODO: Create a program that:
# 1. Takes two numbers as input (as strings)
# 2. Converts them to integers
# 3. Adds them together
# 4. Prints the result in a nice format

# Example output: "5 + 3 = 8"
# Your code here:

# ============================================================================
# EXERCISE 7: If/Else Statements
# ============================================================================
print("Exercise 7: If/Else Statements")
print("-" * 60)
print("Create if/else statements for these scenarios:")
print()

temperature = 25

# TODO: Write an if/else statement that prints:
# "It's hot!" if temperature >= 25
# "It's cool!" otherwise

# Your code here:
# if ???
#     ???
# else:
#     ???

print()

# ============================================================================
# EXERCISE 8: Elif (Multiple Conditions)
# ============================================================================
print("Exercise 8: Elif (Multiple Conditions)")
print("-" * 60)
print("Create an if/elif/else statement:")
print()

score = 85

# TODO: Write an if/elif/else statement that prints:
# "Grade A" if score >= 90
# "Grade B" if score >= 80
# "Grade C" if score >= 70
# "Grade F" otherwise

# Your code here:
# if ???
#     ???
# elif ???
#     ???
# elif ???
#     ???
# else:
#     ???

print()

# ============================================================================
# EXERCISE 9: While Loops
# ============================================================================
print("Exercise 9: While Loops")
print("-" * 60)
print("Create a while loop that counts from 1 to 10:")
print()

# TODO: Write a while loop that prints numbers 1 through 10
# count = 1
# while ???
#     print(count)
#     ???

print()

# ============================================================================
# EXERCISE 10: For Loops
# ============================================================================
print("Exercise 10: For Loops")
print("-" * 60)
print("Create for loops for these scenarios:")
print()

# TODO 1: Loop over a string and print each character
text = "Hello"
# for ???
#     print(???)

# TODO 2: Use range() to print numbers 1 through 5
# for ???
#     print(???)

print()

# ============================================================================
# EXERCISE 11: Tuples - Basics
# ============================================================================
print("Exercise 11: Tuples - Basics")
print("-" * 60)
print("Work with tuples:")
print()

colors = ("red", "green", "blue", "yellow", "orange")

# TODO: Complete these operations:
# 1. Print the first color
# print(colors[???])

# 2. Print the last color (use negative indexing)
# print(colors[???])

# 3. Print the length of the tuple
# print(len(???))

# 4. Check if "blue" is in the tuple
# print(??? in colors)

# 5. Find the index of "green"
# print(colors.index(???))

print()

# ============================================================================
# EXERCISE 12: Tuple Slicing
# ============================================================================
print("Exercise 12: Tuple Slicing")
print("-" * 60)
print("Practice slicing:")
print()

numbers = (10, 20, 30, 40, 50, 60, 70)

# TODO: Create slices that produce:
# 1. Elements from index 1 to 3 (not including 3)
# slice1 = numbers[???]
# print(slice1)  # Should print: (20, 30)

# 2. First 3 elements
# slice2 = numbers[???]
# print(slice2)  # Should print: (10, 20, 30)

# 3. Elements from index 4 to the end
# slice3 = numbers[???]
# print(slice3)  # Should print: (50, 60, 70)

print()

# ============================================================================
# EXERCISE 13: Looping Over Tuples
# ============================================================================
print("Exercise 13: Looping Over Tuples")
print("-" * 60)
print("Loop over a tuple:")
print()

fruits = ("apple", "banana", "cherry", "date")

# TODO: Loop over the tuple and print each fruit with a number
# Example output:
# 1. apple
# 2. banana
# 3. cherry
# 4. date

# Your code here:
# for ??? in fruits:
#     print(???)

print()

# ============================================================================
# EXERCISE 14: Nested Tuples
# ============================================================================
print("Exercise 14: Nested Tuples")
print("-" * 60)
print("Access nested tuple elements:")
print()

students = (("Alice", "Bob"), ("Charlie", "Diana"), ("Eve", "Frank"))

# TODO: Access and print:
# 1. The first inner tuple
# print(students[???])  # Should print: ('Alice', 'Bob')

# 2. "Diana" (second element of second tuple)
# print(students[???][???])  # Should print: Diana

print()

# ============================================================================
# EXERCISE 15: Combined Challenge
# ============================================================================
print("Exercise 15: Combined Challenge")
print("-" * 60)
print("Combine everything you've learned:")
print()

# TODO: Create a program that:
# 1. Creates a tuple of numbers: (5, 10, 15, 20, 25)
# 2. Loops over the tuple
# 3. For each number, checks if it's greater than 10
# 4. Prints "X is greater than 10" or "X is 10 or less"

# Your code here:

print()
print("=" * 60)
print("Great job! Check your answers and try running the code!")
print("=" * 60)

