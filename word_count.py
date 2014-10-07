def main():
      
    script, filename = argv

    print_and_sort_file(read_file(filename))


def read_file(filename):
    word_count = {}

    text = open(filename)
    for line in text:
        line = line.rstrip().lower()
        for punc in string.punctuation:
            line= line.replace(punc," ")
        words = line.split()

# for loop by line: checking for words, adding to dictionary

        for word in words:
            if not word_count.get(word):
                word_count[word] = 1
            else:
                word_count[word] += 1
    return word_count

    # print word_count

def print_and_sort_file(d):
    # print key and value pairs
    for key in sorted(d.keys()):
        print "%s, %d" % (key, d[key])

from sys import argv
import string

if __name__ == "__main__":
    main()