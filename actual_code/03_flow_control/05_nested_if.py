is_sunny = True
temp_in_celcius = 24
has_airconditioning = True

if is_sunny:
  if temp_in_celcius > 20:
    if has_airconditioning:
      print("Whack up the airconditiong! (sorry planet)")
    else:
      print("Try not to melt!")
  print("It's nice outside!")
else:
  print("I like it when it's not sunny.")