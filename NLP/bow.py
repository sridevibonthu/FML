import pandas as pd
import numpy as np

doc1 = 'Game of Thrones is an amazing tv series!'
doc2 = 'Game of Thrones is the best tv series!'
doc3 = 'Game of Thrones is so great'

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([doc1,doc2,doc3])
print(vectorizer.get_feature_names())

df_bow_sklearn = pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names())
print(df_bow_sklearn.head())

