# Module - all files are modules!

def printer(text):
  print("Here is the message:")
  print(text)
  print("Did I do okay?")
  print("=" * 20)

class Shape:
  def __init__(self, type):
    self.type = type

  def __str__(self):
    return f"Shape of type {self.type}"

default_shape = Shape("circle")

def main():
  print("Welcome to the utils module!")
  printer(default_shape)
  print(f"__name__ -> {__name__}")
  print("*=*" * 10)

if __name__ == "__main__": # stand alone code should be in here!
  main()