#STOP WORDS :: used just for removing the not usable words like 'of','the' etc.

from nltk.data import path
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
path.append("F:\\nltk_data")
example_sentence="This is an example showing of stop word filteration"
stop_words=set(stopwords.words("english"))

words=word_tokenize(example_sentence)

#filtered_sentence=[]
#for w in words:
#    if w not in stop_words:
#        filtered_sentence.append(w)
filtered_sentence=[w for w in words if w not in stop_words] #oneliner of above code

print(filtered_sentence)