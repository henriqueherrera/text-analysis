from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize

example = "oi eu sou o henrique, e esse daqui eh um exemplo"
stop_words = set(stopwords.words("portuguese"))
words = word_tokenize(example)

filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)

