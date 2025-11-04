def add(a, b, c=0, d=0):
  return a + b + c + d

# def add_three_numbers(a,b,c):
#   return a + b + c

def add(*numbers):  # ...
  total = 0
  for n in numbers:
    total += n
  return total

# def input():
#   print("No thank you!")



print(add(1, 2))
print(add(4, 4, 5))
print(add(5,4,4,5))