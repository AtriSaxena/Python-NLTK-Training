from nltk.corpus import wordnet

syns= wordnet.synsets("program")

#All realted words
print(syns)

#synset
print(syns[0].name())

#just the name
print(syns[0].lemmas()[0].name())

#defination
print(syns[0].definition())

#examples
print(syns[0].examples())


synonyms=[]
antonyms=[]

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))


#SEMANTIC SIMILARITY

w1= wordnet.synset("ship.n.01")
w2= wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))                                  #wup : woo umparmer : wrote a paper about semantic similarity


w1= wordnet.synset("ship.n.01")
w2= wordnet.synset("car.n.01")
print(w1.wup_similarity(w2))                                  #wup : woo umparmer : wrote a paper about semantic similarity

w1= wordnet.synset("boat.n.01")
w2= wordnet.synset("lion.n.01")
print(w1.wup_similarity(w2))                                  #wup : woo umparmer : wrote a paper about semantic similarity


#########################################
# In online someone copy the article and words with the synonyms or a similar words. And post on their blog as if it is their article.
