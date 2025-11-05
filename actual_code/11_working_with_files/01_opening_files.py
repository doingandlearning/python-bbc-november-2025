# make sure this is running where the file is!

try:
  file = open("test.txt")
  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'> -> handle
except FileNotFoundError:
  print("That file doesn't exist!")

contents = file.read() # reads the file as a string
print(contents)
print(type(contents))

file.seek(0)
contents = file.readlines() # list of each line
print(contents)
print(type(contents))

file.seek(0)
line = file.readline() # reading line by line - gets the next line
while line:
  print(line.strip())
  line = file.readline()

file.close()

