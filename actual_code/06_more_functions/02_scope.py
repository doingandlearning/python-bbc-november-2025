count = 1

def print_count():
  global count  # gives us write access to the variable the outside 
  count = count + 1
  new_total = count + 1
  print(f"Count inside the function {count}")
  return new_total


print(f"Count outside the function (and before the call) {count}")
print_count()
print(f"Count outside the function (and after the call) {count}")


# 1. Functions can read variables outside themselves!
# 2. 'Shadowing' is when a variable in a function gets priority over the version 
# of the same variable name outside the function.
# 3. Variables created inside a function can't be accessed outside!