import random 

secret_channel = random.randint(1,50)

# Print welcome message
print("Welcome to the BBC Channel Guessing Game!")
print("I'm thinking of a channel number between 1 and 50.")
print("You have 5 tries to guess it!")

player_won = False
attempts = 0

def get_valid_value():
  while True:
    try:
      guess = int(input("Enter your guess (1-50): "))
      return guess
    except ValueError:
      print("Whoops! You tried to enter something that wasn't a number.")

while attempts < 5:
  print(f"Attempt {attempts +1 }")
  guess = get_valid_value()
  if guess == secret_channel:
    print("🍻 Well done! You got it!")
    player_won = True
    break
  elif guess < secret_channel:
    print("Whoops! Too low.")
  elif guess > secret_channel:
    print("Whoops! Too high!")
  attempts += 1

if player_won:
  print("You did well - come back play again soon!")
else:
  print(f"Sorry you lost, the right answer was {secret_channel}. Come back again soon!")