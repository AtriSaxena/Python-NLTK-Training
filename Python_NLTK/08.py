#LEMMATIZER: To get synonym of word.

import nltk
from nltk.stem import WordNetLemmatizer

nltk.data.path.append("F:\\nltk_data")
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("better",pos="a"))