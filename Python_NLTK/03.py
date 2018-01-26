#STEMMING: Remove suffix & use 1st form. like 'Running' to 'Run'
from nltk.data import path
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
path.append("F:\\nltk_data")
ps=PorterStemmer()
st=SnowballStemmer("english")
example_words=["python","pythoner","pythoning","pythoned","pythonly"]

#for w in example_words:
#    print(ps.stem(w))

new_text="It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly atleast once."
words=word_tokenize(new_text)

for w in words:
    print(st.stem(w))


## LOOKOUT

    #HUNSPELL stemmer
