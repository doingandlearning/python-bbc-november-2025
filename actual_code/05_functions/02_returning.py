def add(num1, num2):
  "Adds two numbers together"
  total = num1 + num2
  return total

print(add(1,2))

def get_readings_from_user():
  """
  Return a list of values from a user.
  """
  readings = []

  while True:
    reading = input("Please enter reading (q to quit): ")
    if reading == "q":
      break
    readings.append(reading)
  return readings














print(get_readings_from_user())
# DRY - Don't Repeat Yourself  - Rule of 3