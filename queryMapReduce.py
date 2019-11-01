import re
import sys
import json
import collections
from collections import defaultdict
invertedIndex = defaultdict(lambda: defaultdict(list))
#load the file

#this file is  to implement boolean search  with the inverted Index created using mapreduce
with open("indexMapReduce.json") as jsonFile:
    invertedIndex = json.load(jsonFile)

#function to evaluate the query given
def infixQuery(query):
    booleanWords = ['and', 'or']
    lowerCase = query.lower()
    lowerCase = re.sub(r'[^\w\s]', '', lowerCase)
    listOfQuery = lowerCase.split()
    numWords = len(listOfQuery) % 2
    #if num words queried is even: there is an error, because carrot and peach has 3 words, but carrot and has 2
    if (numWords == 0):
        print("sorry, you have entered an invalid query")
        return
    #if it's only one word, return # the result now
    if(len(listOfQuery) == 1):
        word = listOfQuery[0]
        #if one word is given and it's not in our  index, return this fact
        docs = getLength(word)
        if(len(docs) > 0):
            for x in range (0, len(docs)):
                print(word + " is in document: " + docs[x])
            return

        else:
            printList(docs)
            return
    termStack = list()
    i = 0
    while (i<len(listOfQuery)):
        currentWord = listOfQuery[i]
        if(currentWord not in booleanWords):
            #add it to the termStack
            termStack.append(currentWord)
        #if word is equal to and or or
        else:
            operation = currentWord
            i += 1
            newWord = listOfQuery[i]
            #if query is carrot and and, then print the query has an error
            if(newWord in booleanWords):
                print("error, your query is invalid because you used  two boolean words in a row!")
                del termStack[:]
                return
            previous = termStack.pop()
            termStack.append(executeQuery(operation,previous,newWord))
        i += 1
    #the only thing on the stack is our result
    finalResult = termStack.pop()
    return printList(finalResult)

#print out the documents thatt matched the queries
def printList(list):
    #if list is empty return that
    if (list == "none" or len(list) == 0):
        print("sorry, your query returned no documents!")
        return
    result= ''
    for element in list:
        result += " " + str(element) + ","
    print("the documents found matching your query are: " + result)
    return
#function to remove duplicates from a list
def removeDuplicates(duplicateList):
    final_list = []
    for num in duplicateList:
        if num not in final_list:
            final_list.append(num)
    return final_list

#returns index list of documents, or an empty list
def getLength(string1):
    try:
        x = list(invertedIndex[string1].keys())
        return x
    except KeyError:
        x = []
        return x

#function to find documents in the two lists
def findDocuments(operation, listOne, listTwo):
    newList = []
    listOne.sort()
    listTwo.sort()
    i = 0
    j = 0
    if(operation == "and"):
        while (i < len(listOne) and j < len(listTwo)):
            if (listOne[i] == listTwo[j]):
                newList.append(listOne[i])
                i += 1
                j += 1
            elif(listOne[i] > listTwo[j]):
                j += 1
            else:
                i += 1
        return removeDuplicates(newList)
    elif(operation == "or"):
        while(i < len(listOne)):
            newList.append(listOne[i])
            i+=1
        while(j < len(listTwo)):
            newList.append(listTwo[j])
            j+=1
        newList.sort()
        return removeDuplicates(newList)
#function that returns documents containing term 1 and term 2
def executeQuery(operation,term1, term2):
    #term1 and term2 can either be a list of documents, or a string of a word we want to find.
    #eg if we are looking for (Fox And Dolphin) And Whale, term1 would be a list of documents matching fox and dolphin, and term 2 would be the string whale
    operation2 = operation.lower()
    #if both terms are strings
    if(isinstance(term1,str) and isinstance(term2,str)):
        #if both are found
        documentsTermOne = getLength(term1)
        documentsTermTwo = getLength(term2)
        return(findDocuments(operation2, documentsTermOne, documentsTermTwo))
    #if term2 is a string
    elif(isinstance(term1,list) and isinstance(term2, str)):
        documentsTermTwo = getLength(term2)
        return(findDocuments(operation2, term1, documentsTermTwo))


#while loop to continuously grab query input from the user
while True:
    query = raw_input("Enter Your Query: ")
    infixQuery(query)
