#this program uses the output of reducer.py in order to build an inverted index
#program assumes that input is a file of output to reducer.py
from collections import defaultdict
import re
import json
import sys
invertedIndex = defaultdict(lambda : defaultdict(list))

for line in sys.stdin:
    line = line.strip()
    word, document = re.split('\t+', line)
    word = re.sub(r'[^\w\s]', '', word)
    invertedIndex[word][document] = 1
#now that we have built the  index,  save it
indexDoc = open('indexMapReduce.json', "w")
json.dump(invertedIndex, indexDoc)
indexDoc.close()