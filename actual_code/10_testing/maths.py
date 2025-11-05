def add(a, b):
  # if "a is not a float or int or b is not a float or an int":

  if not isinstance(a, (int, float)) or not isinstance(b, (float, int)):
    raise TypeError("Both arguments must be numbers.")
  return a + b


# pip install pytest-cov
# pytest --cov