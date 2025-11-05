import traceback

def divide_numbers(a, b):
  try:
    # raise SyntaxError("Invalid syntax")
    # int("Four")  # raise
    return a / b
  except ArithmeticError:
    print("You tried to divide by zero!")

try:
  print(divide_numbers(4, 2))
  # int("four")
  print(divide_numbers(10, 0))
  print(divide_numbers(1, -2))
except ArithmeticError as error:
  print("Whoops! You tried to divide by zero.") # this is the message to the user
  print(error) # log, SNS, ... email the ops
  traceback.print_exc()
except ValueError:
  print("You tried to convert something that wasn't a digit.")
except Exception as error: 
  print("Something unexpected went wrong!") # a nice user message ... 
  print(error)
  traceback.print_exc()

print("I'm still here!")

