from nltk.stem.porter import PorterStemmer
from math import *
from heapq import *


stemmer = PorterStemmer()

def main():
    documents = {2 : 'Cybersecurity.txt', 3 : 'IndustrialRevolution.txt', 4 : 'Reverse_engineering.txt', 5 : 'arteficial_intellegence.txt',6 : 'crypto_currency.txt', 7 : 'Digital_Marketing.txt', 8: 'Machinelearning.txt',9 : 'Social_Media_Marketing.txt',10 :'climate_change.txt', 11 :  'information_retrival.txt'}



    stemmer = PorterStemmer()


    query = input().split()

    for i, term in enumerate(query):
        word = stemmer.stem(term)
        query[i] = word

    freq = {}
    for term in query:
        freq[term] = freq.get(term, 0) + 1

    terms = []
    vspm = {}

    with open('C:/Users/Toshiba/desktop/cse/searchengine/indexing/index_term.txt', 'r') as file:
        for line in file:
            take = line.strip().split("##")
            p = [take[0], int(take[1])]
            k = take[2][1:-1].split(',')
            p.append(k)
            terms.append(p)

    for term in terms:
        lst = [0]*12
        word = term[0]
        lst[1] = freq.get(word, 0)
        lst[0] = int(term[1])
        for f in term[2]:
            st = f.split(':')
            lst[int(st[0]) + 2] = int(st[1])
            vspm[word] = lst

    tfidf = {}

    for key, value in vspm.items():
        lst = [0]*12
        lst[0] = log(10/value[0])
        for i in range(1, 12):
            lst[i] = lst[0] * value[i]

        tfidf[key] = lst


    cossimilarity = [0]*12


    for i in range(1, 12):
        temp = 0
        for val in tfidf.values():
            temp += val[i]*val[i]

        cossimilarity[i] = sqrt(temp)

    if cossimilarity[1] == 0:
        print("oops No match found!!")
        return

    lst = [0]*12
    for i in range(1, 12):
        temp = 0
        for key, val in tfidf.items():
            temp += val[1]*val[i]

        lst[i] = temp/(cossimilarity[i]*cossimilarity[1])

    heap = []
    for i, val in enumerate(lst):
        heappush(heap, (-val, i))

    while heap:
        _, i = heappop(heap)
        if i < 2:
            continue

        print(documents[i])




main()







