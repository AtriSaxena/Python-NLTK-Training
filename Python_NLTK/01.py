import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
nltk.data.path.append("F:\\nltk_data")
#Tokenizing : word tokenizers & sentence tokenizer
#lexicons & corporas
#corpora- body of text. eg. MEdical journals, presidential speech, English language
#lexicon- words & their meaning


#Investor speak vs regular English speak
#investor speak 'bull': someone who is positive about the market
#English speak 'bull': scary animal who dont want running

example_text="Hello Mr. Smith, how are you doing today? The weather is great and python is awesome. The sky is pinkish-blue. You should not eat cardboard."

print(sent_tokenize(example_text))
print(word_tokenize(example_text))
