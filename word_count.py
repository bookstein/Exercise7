from sys import argv

# import string


# import file, open file
# assign arguments
script, filename = argv

text = open(filename)

word_count = {}

# for loop by line: checking for words, adding to dictionary
for line in text:
    line = line.rstrip().lower()
    # for char in line:
    #     if char in string.punctuation:
    #         char = " "
    words = line.split()

    for word in words:
        if word not in word_count.items():
            word_count[word] = 1
        else:
            word_count[word] += 1

print word_count
#get the word, increment the instances of each word
#make the word a key and add the number of instances as a value







