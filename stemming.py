from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["oi", "Ola", "oie", "oiiiii"]

new_text = "oi eu so sei falar oie mas gosto de falar oiiii falando oieee"

words = word_tokenize(new_text)

for w in words:
  print(ps.stem(w))