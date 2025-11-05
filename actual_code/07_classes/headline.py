class Headline:
  """
  This is a documentation string
  """
  def __init__(self, text, source):
    self.text = text
    self.source = source
    self.url = ""

  def __str__(self):
    return f"'{self.text}' - [Source: {self.source}]"

  def get_word_count(self):
    words = self.text.split()
    return len(words)

headline1 = Headline("Unsurprisingly it rains in Belfast", "Kevin")
print(headline1)
print(headline1.text)

print(headline1.get_word_count())

# .is_long_headline()
Headline()