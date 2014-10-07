from sys import argv

import string

script, filename = argv

text = open(filename)

word_count = {}

# for loop by line: checking for words, adding to dictionary
for line in text:
    line = line.rstrip().lower()
    for punc in string.punctuation:
        line= line.replace(punc," ")
    words = line.split()


    for word in words:
        if not word_count.get(word):
            word_count[word] = 1
        else:
            word_count[word] += 1

# print key and value pairs
keys_list = word_count.keys()


for word in sorted(word_count, key = word_count.get, reverse = True):
    print "%s, %d" % (word, word_count[word])