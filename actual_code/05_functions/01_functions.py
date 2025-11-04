# print("Hello")
# input("Number: ")

def print_hello():
  print("=" * 20)
  print("Hello!")
  print("=" * 20)

# Abstraction

print_hello()


def say_hello_to_user(name, seperator="=", width=20):  # positional argument
  """
  A function to say hello to a user with seperators
  Arguments:
    - name
    - seperator (defaults to =)
    - width (defaults to 20)
  """
  min_width = 20
  width = max(min_width, width)
  print(seperator * width)

  print(f"Hello {name}")
  print(seperator * width)

say_hello_to_user("Brodie", width=25)
say_hello_to_user("Andy", "*", 15)
get_user_value = say_hello_to_user(name="Chris", seperator="+", width=10)

print(get_user_value)

