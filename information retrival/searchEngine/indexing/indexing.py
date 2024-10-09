from collections import *
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer
import nltk
import re


stemmer = PorterStemmer()

def makelower(word):
    text = ['']

    for ch in word:
        if ch.isalpha():
            text.append(ch)

    return "".join(text)

def stem_doc(content):
    stemed = []
    for word in content.split():
        word = word.lower()
        tokens = makelower(word)
        tokens = "".join(nltk.word_tokenize(tokens))
        stemed.append(stemmer.stem(tokens))

    return stemed


documents = ['Cybersecurity.txt', 'IndustrialRevolution.txt', 'Reverse_engineering.txt', 'arteficial_intellegence.txt', 'crypto_currency.txt', 'Digital_Marketing.txt',  'Machinelearning.txt', 'Social_Media_Marketing.txt',  'climate_change.txt',  'information_retrival.txt']


inverted_index = defaultdict(dict)

for idx, document in enumerate(documents):
    with open('corpus/' + document, 'r') as file:
        contents = file.read()

    words = stem_doc(contents)

    for word in words:
        inverted_index[word][idx] = inverted_index[word].get(idx, 0) + 1



inverted = sorted(inverted_index)

with open("index_term.txt", "w") as file:
    for word in inverted:
        file.write(word + "##" + str(len(inverted_index[word])) + "##" + str(inverted_index[word]) + "\n")

    




