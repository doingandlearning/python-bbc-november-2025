first_name = "Kevin"
last_name = "Cunningham"

# concatenation -> joining strings together
full_name = first_name + " " + last_name
print(full_name)

full_name = f"{first_name} {last_name}"
print(full_name)

print(f"1 + 1 = {1 + 1}")  # f-strings -> "formatted string"

print(full_name.capitalize())
print(full_name.upper())
print(full_name.center(100))

print(full_name.find("in"))

#0123456789
"Kevin Cunningham"
print(len(full_name))

print("I don't know")
print('He said, "Hello how are you?"')
print(f''' Hello {full_name} 
How are you?
I'm fine''')