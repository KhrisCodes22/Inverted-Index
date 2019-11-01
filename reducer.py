#!/usr/bin/env python
#code for the reducer class in python
import re
from sys import __stdin__, stdin
from collections import defaultdict
currentWord = None
currentDocument = None
for line in stdin:
    line = line.strip()
    word, document = re.split('\t+', line)
    #if word matches
    if(currentWord == word):
        #if document doesn't match, print out the previous document
        if(currentDocument != document):
            print('%s\t%s' % (currentWord, currentDocument))
            #update document
            currentDocument = document
    else:
        if(currentWord):
            #since words don't match, print out the last word/doc pair
            print('%s\t%s' % (currentWord, currentDocument))
            currentWord = word
            currentDocument = document
        #if current word is none?
        currentWord = word
        currentDocument = document
print('%s\t%s' % (currentWord, currentDocument))


