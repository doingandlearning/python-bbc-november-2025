user_channel = input("What channel would you like to watch? ").lower().strip()

# if is_bbc_one(user_channel):
if user_channel == "bbc 1" or user_channel == "bbc1":
  print("Are the traitors going to win?")
elif user_channel == "bbc 2":
  print("Time for University Challenge")
elif user_channel == "cbeebies":
  print("It's time for Bluey")
elif user_channel.startswith("bbc"):
  print("I like that channel!")
else:  # fallback -> if nothing else matches!
  print("I don't know that channel.")

# Pi-thon
match user_channel:
  case "bbc1" | "bbc 1":
    print("Are the traitors going to win?")
  case "bbc2" | "bbc 2":
    print("Time for University Challenge") 
  case "cbeebies":
    print("It's time for Bluey") 
  case _:
    print("I don't know that channel")