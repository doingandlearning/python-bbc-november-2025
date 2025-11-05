import csv

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

with open("movies.csv", mode="a") as file:
  writer = csv.writer(file)
  writer.writerow(["K-Pop Demon Hunters", 2025, "Maggie Kang;Chris Appelhans", "Animation"])