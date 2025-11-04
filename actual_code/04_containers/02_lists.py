empty_list = []
empty_list = list()
# tuple()

print(empty_list)
print(type(empty_list))  # JS -> array

beatles = ["John", "Paul", "George", "Ringo"]  

print(len(beatles))
print(beatles[1])
print(beatles[1:])

print("John" in beatles)
print("Kevin" in beatles)

for band_member in beatles:
  print(band_member.lower())

for band_member in beatles:
  print(band_member.upper())

beatles.append("Jules")  # a single item 
print(beatles)

beatles.extend(("Zaid", "Darren", "John")) # add multiple items
print(beatles)

beatles.insert(0, "Hussain") # adds a single item at a specific position - costs more!
print(beatles)

beatles.remove("John")  # the first!

while "John" in beatles:
  beatles.remove("John")

print(beatles)

beatles[1] = None
print(beatles)

beatles[1] = "Siobhan"
print(beatles)

beatles.sort()
print(beatles)

beatles.reverse()
print(beatles)

bands = [
    ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"],      # Queen
    ["Kurt Cobain", "Krist Novoselic", "Dave Grohl"],                     # Nirvana
    ["Mick Jagger", "Keith Richards", "Charlie Watts", "Ronnie Wood"],   # The Rolling Stones
    ["Beyoncé", "Kelly Rowland", "Michelle Williams"],                   # Destiny's Child
    ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],  # The Beatles
    ["Thom Yorke", "Jonny Greenwood", "Colin Greenwood", "Ed O'Brien", "Phil Selway"],  # Radiohead
    ["Bono", "The Edge", "Adam Clayton", "Larry Mullen Jr."],            # U2
    ["Chris Martin", "Guy Berryman", "Jonny Buckland", "Will Champion"], # Coldplay
    ["Debbie Harry", "Chris Stein", "Clem Burke", "Jimmy Destri"],       # Blondie
    ["Jack White", "Meg White"]                                          # The White Stripes
]

print(bands[7][1])
print(bands[2][3])