#!/usr/bin/env python
#this file is to create an inverted index using MapReduce
import re
import os
import sys
stopwords = ["and", "but", "is", "the", "to"]

#function to get what file we are currently in
def getFileName():
    name = os.environ['map_input_file']
    parts = name.split('/')
    length = len(parts)
    filename = parts[length - 1]
    return filename

#main function to emit txt to be sorted by hadoop
for line in sys.stdin:
    words = line.strip().split()
    for i in range(0, len(words)):
        name = getFileName()
        word = words[i]
        word = word.lower()
        currentWord = re.sub(r'[^\w\s]', '', word)
        #if a proper word is found.
        if ((currentWord not in stopwords) and currentWord.isdigit() == False and len(currentWord) != 0):
            print("%s\t%s" % (word, name))

