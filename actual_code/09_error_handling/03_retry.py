class InvalidUserInputError(Exception):
  pass


def get_valid_user_input():
  try:
    user_input = input("What's your favourite broadcasting network?")
    if user_input.lower() != "bbc":
      raise InvalidUserInputError("That's wrong - try again!")
    return user_input
  except InvalidUserInputError as error:
    print(error)
    return get_valid_user_input()

print(get_valid_user_input())

def get_valid_user_input():
    user_input = input("What's your favourite broadcasting network?")
    if user_input.lower() != "bbc":
      print("That's wrong - try again!")
      return get_valid_user_input()
    return user_input

print(get_valid_user_input())