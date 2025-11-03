user_input = input("what is your password? ")
password = "password123"
attempts_tried = 0
is_out_of_tries = False
authorized = False

while user_input != password:  # I don't know how many times!
  print("Unauthorized. Please try again.")
  # attempts_tried = attempts_tried + 1
  attempts_tried += 1
  if attempts_tried == 3:
    print("All out of tries!")
    is_out_of_tries = True
    break
  user_input = input("What is your password.")

if is_out_of_tries is False:
  authorized = True 

if authorized:
  print("Here are your secret documents.")