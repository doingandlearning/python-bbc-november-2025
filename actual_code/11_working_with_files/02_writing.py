file = open("time.log", mode="a")

# r -> read
# w -> write
# a -> append

file.write("Hello!\n")
file.write("How are you?\n")
file.write("I'm so tired ... was this course really only 3 days?\n")


file.close()

with open("time.log", mode="a") as file:
  file.write("I'm here too\n")