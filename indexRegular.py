#function to add stuff to the inverted index.
#this stuff works for 1 document, edit it so that it works for 2 documents
import sys
import re
from collections import defaultdict
import os
import json
import glob
stopwords = ["and", "but", "is", "the", "to"]

invertedIndex = defaultdict(lambda: defaultdict(list))
documentsToProcess = glob.glob('*.txt')
for k in range(0, len(documentsToProcess)):
    document = documentsToProcess[k]
    File = open(documentsToProcess[k], "r")
    tokens = File.read().split()
    #go thru the document you've been given
    for i in range(0, len(tokens)):
        currentWord = tokens[i]
        #remove non alphanumeric characters like .,$# etc
        currentWord = re.sub(r'[^\w\s]', '', currentWord)
        currentWord = currentWord.lower()
        #check stopwords and numbers
        if((currentWord not in stopwords) and currentWord.isdigit() == False and len(currentWord) != 0):
            position = i + 1
            invertedIndex[currentWord][document].append(position)
            #self.counterIndex[currentWord] = len(list(self.invertedIndex[currentWord].keys()))
            #if we have a number or a stopword, we don't add it to our index
        else:
            position = i + 1
indexDoc = open('indexRegular.json', "w")
json.dump(invertedIndex, indexDoc)
indexDoc.close()


