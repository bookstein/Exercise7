from sys import argv

import string


# import file, open file
# assign arguments
script, filename = argv

text = open(filename)

word_count = {}

# for loop by line: checking for words, adding to dictionary
for line in text:
    line = line.rstrip().lower()
    for punc in string.punctuation:
        line= line.replace(punc,"")
    words = line.split()


    for word in words:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1


# print word_count
#get the word, increment the instances of each word
#make the word a key and add the number of instances as a value



# print key and value pairs
for key, value in word_count.items():
    print "%s, %d" % (key, value)