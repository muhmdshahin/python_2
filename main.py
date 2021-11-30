# Submitted by Muhammed Shahin Mohammed Ali Ayanippurath
# Student no : mm117408
# Date : 30-11-2021

# Program to find the number of words in a text file

# open the file and read the file content as a string, and save it to variable file content
fileContent = open("input.txt", "r").read().replace("\n", " ").replace("\t", " ")

# split the file content string by white spaces to get an array of words, save it to variable words
words = fileContent.split()

# declare a dictionary wordDict
wordDict = dict()

# for each word in words array, check the keys of the dictionary. if found, increment the value of the particular key.
# if not found, assign a key for this word and keep it's value as 1
for word in words:
    if word in wordDict:
        wordDict[word] += 1
    else:
        wordDict[word] = 1
# the number of items in the words array gives the word count of the file
print(wordDict)
