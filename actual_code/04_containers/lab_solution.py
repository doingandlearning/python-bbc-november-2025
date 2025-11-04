headlines = [
    "General election: Labour and Tories clash over tax",
    "England crowned T20 world champions",
    "Summer travel chaos feared as airline strikes loom",
    "UK inflation rate falls to lowest level in three years",
    "New David Hockney exhibition opens in London",
    "Science discovers new way to tackle plastic waste",
    "Government announces new funding for NHS",
    "Stock market hits record high on tech boom",
    "Debate rages over future of Artificial Intelligence",
    "Classic Doctor Who episodes to be released in colour",
    "Licence fee goes up"
]

total_headlines = len(headlines)

# mean length 
total_words = 0
for h in headlines:
  words = h.split()
  # total_words = total_words + len(words)
  total_words += len(words)

mean_average = total_words / total_headlines
print(total_words, total_headlines)
print(round(mean_average, 2))
print(f"{mean_average:.4f}")

user_keyword = input("What do you want to search for? ").lower().strip()

match_count = 0
matching_headlines = []
for h in headlines:
  if user_keyword in h.lower():
    matching_headlines.append(h)

print(f"We matched {user_keyword} in {len(matching_headlines)} headlines.")
for h in matching_headlines:
  print(f"- {h}")