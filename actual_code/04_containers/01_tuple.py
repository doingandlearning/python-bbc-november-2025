name_1 = "Maddy"
name_2 = "Siobhan"
name_3 = "Jules"

#           0         1         2         3       4
names = ("Maddy", "Siobhan", "Jules", "Chris", "Darren")  # immutable - unchangeable 

print(names)
print(type(names))

for first_name in names:  # loop over a tuple
  print(f"{first_name} works at the BBC")


# check for membership
print("Kevin" in names)
print("Maddy" in names)

print(names.count("Rahul"))
print(names.index("Siobhan"))

if "Hussain" in names:
  print(names.index("Hussain"))

# How many elements in the tuple.
print(len(names))

print(names[3])  # get the element at that position (at that index)

#           0         1         2         3       4
# names = ("Maddy", "Siobhan", "Jules", "Chris", "Darren")  # immutable - unchangeable 

print(names[1:3])   # [a:b] from a to b - not including b
print(names[2:4])
print(names[:3])
print(names[2:])


more_names = (names, ("Zaid", "Andy", "Brodie"), ("Rahul", "Olamide", "Hussain"))

print(more_names)

# Olamide
print(more_names[2][1])