import nltk
from nltk.corpus import stopwords
print(stopwords.words('english'))


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
  
example_sent = """We are learning Natural Language Processing as part of
                Fundamentals of Machine Learning in our second year B.Tech."""
  
stop_words = set(stopwords.words('english'))
  
word_tokens = word_tokenize(example_sent)
  
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  
filtered_sentence = []
  
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
  
print(word_tokens)
print(filtered_sentence)
