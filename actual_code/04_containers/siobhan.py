headlines = [
 
"Claim UK university stopped research after China pressure referred to counter-terror police",
"Reeves refuses to rule out tax rises in Budget as she says she will make 'necessary choices'",
"Chris Mason: Could Reeves break a 50-year taboo by raising income tax?",
"The 20 terrifying minutes endured by train attack passengers",
"New Attenborough doc captures lion saving pregnant hyena from wild dogs",
"How Trump is making the White House in his own image",
"'I've not written this to tear anyone down': Ex-England keeper Mary Earps on book backlash",
"More people using family help than Buy Now Pay Later loans - but even that can come at a cost",
"'I've been using sick days to get fertility treatment' - calls for legal right to paid leave for IVF",
"Couple took in six passengers after train attack",
"Trump backs Cuomo for New York City mayor and threatens to cut funding if Mamdani wins",
"We are ready to discuss human rights law changes, top ECHR boss tells BBC"]
 
#counting the headlines
total_headlines = len (headlines)
print (total_headlines)
 
#average headline length
total_words_in_headlines = 0
for headline in headlines:
  words = headline.split()
  print(f"'{headline}' is {len(words)} words long")
  total_words_in_headlines += len(words)

print(total_words_in_headlines)

 
 