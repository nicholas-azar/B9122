# Problem #1
# use .replace to replace and return the word
def replace(word):
    word = word.replace("a" , "i")
    return word

# Problem #2
# create a nested for loop to go through the n^2 calculations and print it
def multiply(n):
    for i in range(1,n+1):
        for j in range(1, n+1):
            ans = i*j
            print(i,'*', j,'=',ans , sep = '')
    
# Problem #3
# split the text up into individual words
# create another list with the length of each word in order
# zip the 2 lists to make tuples, sort it and return it
def wordSort(string):
    words = string.split()
    length = []
    for x in words:
        length.append(len(x))
    tuples = sorted(list(zip(length,words)))
    return(tuples)

# Problem #4
# Make the text lowercase, split the text and count the word occurances in a dict
# Then make lists with the top 5 words and the occurances of each
# Print out the occurances for each of the top 5 words
def countOccurances():
    fh = open('question4.txt')
    text = fh.read()
    lowText = text.lower()
    words = lowText.split()
    d = {}
    occurance =[]
    for x in words:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
    sortWords = sorted(d, key=d.get, reverse=True)[:5]
    
    for x in sortWords:
        occurance.append(d[x])

    for i in range(len(occurance)):
        print(occurance[i], sortWords[i])
    


# Problem #5a
import re
def dateMatch(text):
    match = re.search('(\d{4})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])', text)
    print(match.group(0))

# Problem #5b
def zipMatch(text):
    match = re.findall('\d{5}(?!-)|\d{5}-\d{4}', text)
    return match

# Problem #5c
def emailMatch(text):
    match = re.findall('\w+@\w+\.com', text)
    return match


# Problem #6
# create an empty list and fill it only with the index locations where a = b and return it
import numpy as np
def indexMatch(a = np.array([1, 2, 3, 2]), b = np.array([2,2,2,2])):    
    matchingIndices = []
    for i in range(len(a)):
        if a[i] == b[i]:
            matchingIndices.append(i)
    
    return matchingIndices

    
