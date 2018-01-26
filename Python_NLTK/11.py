#TEXT CLASSIFICATION

import nltk
import random
from nltk.corpus import movie_reviews

#one liner example
#documents=[(list(movie_reviews.words(fileid)),category)         #list of tuples
#           for category in movie_reviews.categories()
 #          for fileid in movie_reviews.fileids(category)]

#multiliner example
documents=[]
for category in movie_reviews.categories():             #it contain all the words which has class label as positive or negative
    for fileid in movie_reviews.fileids(category):
        documents.append(list(movie_reviews.words(fileid),category))


random.shuffle(documents)       #bcz postive and negative example are together...1000 postivie than 1000 negative

#print(documents[1])

all_words=[]

for w in movie_reviews.words():         #append all the words in a list. so that we can classify.
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
#print(all_words.most_common(10))

print(all_words["good"])
print(all_words["bad"])
print(all_words["awesome"])
