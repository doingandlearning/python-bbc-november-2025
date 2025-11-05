user1 = {
  "name": "Chris",
  "location": "Wigan",
  "team": "Recommendations",
  "role": "PM"
}

user2 = {
  "nae": "Brodie",
  "location": "London",
  "taem": "AI Innovation",
  "role": "Apprentice"
}

class User:
  def __init__(self, name, location, team, role="Unknown"):
    self.name = name
    self.location = location
    self.team = team
    self.role = role


  def __str__(self):
    return f"User(name={self.name}, location={self.location}, team={self.team}, role={self.role})"
  
  def introduce_self(self):
    print(f"Hi, I'm {self.name}. I'm a {self.role} in the {self.team} team living in {self.location}.")

  def is_weekend(self, day):
    match day:
      case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        return False
      case _:
        return True

  # double underscore -> dunder methods

user3 = User(name="Jules", location="Reading", team="BBC Monitoring")  
user4 = User("Zaid", "Salford", "Catalogue", "Developer Engineer")

# list() str() int()  -> making an instance -> instantiating, initialising
print(user3)  # What class are you? __str__ ? __repr__ ?  __str__
print(user4)
print(user3.name)
print(user4.name)

user3.introduce_self()
user4.introduce_self()

print(user3.is_weekend("Monday"))
print(user4.is_weekend("Saturday"))

str()