number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


doubled_numbers = []
for number in number_list:
  if number < 7:
    doubled_numbers.append(number * 2)

print(doubled_numbers)

doubled_numbers = [number * 2 for number in number_list 
                              if number < 7
                  ] # List Comprehension
print(doubled_numbers)  # Map   x -> y

names = ["Brodie", "Siobhan", "Chris", "Hussain", "Maddy"]
upper_names = [name.upper() for name in names]
print(upper_names)