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
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1

# print key and value pairs
for key, value in sorted(word_count.iteritems()):
    print "%s, %d" % (key, value)