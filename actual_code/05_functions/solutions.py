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
    "Classic Doctor Who - episodes to be released in colour",
    "Licence fee goes up"
]

def get_word_count(headline):
  """
    Count the number of words in a headline.
    
    Args:
        headline_text (str): The headline to count words in
        
    Returns:
        int: The number of words in the headline
  """
  words = headline.split()
  return len(words)


total_headlines = len(headlines)
# mean length 
total_words = 0
for h in headlines:
  total_words += get_word_count(h)

mean_average = total_words / total_headlines
print(total_words, total_headlines)
print(round(mean_average, 2))
print(f"{mean_average:.4f}")


def find_headlines_with_keyword(headlines, keyword):
  matching_headlines = []
  for h in headlines:
    if keyword.lower() in h.lower():
      matching_headlines.append(h)
  return matching_headlines


while True:
  user_keyword = input("What do you want to search for? ").lower().strip()
  if user_keyword == "q":
    break
  matching_headlines = find_headlines_with_keyword(headlines, user_keyword)

  print(f"We matched {user_keyword} in {len(matching_headlines)} headlines.")
  for h in matching_headlines:
    print(f"- {h}")