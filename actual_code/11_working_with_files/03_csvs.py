import csv
import json

# with open("movies.csv") as file:
#   reader = csv.reader(file)
#   next(reader)
#   for title, year, director, genre in reader:
#     print(f"{title} was made in {year}, directed by {director} in the genre {genre}")

# with open("movies.csv") as file:
#   reader = csv.DictReader(file, fieldnames=["title", "year", "director", "genre"])
#   next(reader)
#   for row in reader:
#     print(f"{row.get("title")} was made in {row.get("year")}, directed by {row.get("director")} in the genre {row.get("genre")}")

# with open("movies.csv", mode="a") as file:
#   writer = csv.writer(file)
#   writer.writerow(["K-Pop Demon Hunters", 2025, "Maggie Kang;Chris Appelhans", "Animation"])

movies = []

with open("movies.csv") as file:
  reader = csv.DictReader(file)
  for movie in reader:
    movies.append(movie)

musicals = [movie for movie in movies if movie["Genre"] == "Musical"]
recent_movies = [movie for movie in movies if int(movie["Year"]) > 2020] 

with open("movies.json", "w") as file:
  json.dump(recent_movies, file, indent=2)

