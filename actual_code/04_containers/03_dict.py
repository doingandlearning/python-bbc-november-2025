empty_dict = {}

print(empty_dict)
print(type(empty_dict))  # key/value pairs

user_dict = {
  "team": "Product Support",
  "name": "Rahul",
  "goals": ["Understand Python", "Work with old VMs", "Link to SQL and Powershell"]
}

print(user_dict["name"])
user_dict["name"] = "Rahul Soni"
print(user_dict.get("first_name"))  # get the value for this key
user_dict["previous_programming"] = ["SQL", "Powershell"]

print("name" in user_dict)  # be careful! `in` is checking against the keys
print("Rahul" in user_dict)

print(user_dict.keys())
print(user_dict.values())
print(user_dict.items())

for key in user_dict.keys():
  print(key)

for value in user_dict.values():
  print(value)

for item in user_dict.items():
  print(f"{item[0]} => {item[1]}")