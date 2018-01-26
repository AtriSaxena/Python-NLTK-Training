#TEXT CLASSIFICATION

import nltk
import random
from nltk.corpus import movie_reviews
import pickle

documents=[(list(movie_reviews.words(fileid)),category)         #it contain all the words which has class label as positive or negative
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)       #bcz postive and negative example are together...1000 postivie than 1000 negative

all_words=[]

for w in movie_reviews.words():         #append all the words in a list. so that we can classify.
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features= list(all_words.keys())[:3000]

def find_features(document):
    words=set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

#print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

featuresets = [(find_features(rev),category) for (rev,category) in documents]
print(featuresets[0:10])

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

#classifier= nltk.NaiveBayesClassifier.train(training_set)

classifier_f= open("naivebayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Naive Bayes Algo accuracy in %: ", nltk.classify.accuracy(classifier, testing_set)*100)
classifier.show_most_informative_features(15)

#using pickle to save the classifier so that it is not needed again to classify the algo nd save time when re-run
#save_classifier = open("naivebayes.pickle","wb")
#pickle.dump(classifier, save_classifier)
#save_classifier.close()