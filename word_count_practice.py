""" This is a practice redo of Exercise 7 from Monday 10/6.
Working on it on Friday 10/10.
How long does it take me to complete the exercise?"""

import string
from sys import argv
# open and read in file -- no need to do it line by line
# lowercase, punctuation, line split

def read_file(filename):

	dictionary = {}

	f = open(filename)
	text = f.read()

	# format text
	text = text.lower()
	words = text.split()

	for word in words:
		dictionary[word] = dictionary.get(word, 0) + 1 # increments value by 1

	return dictionary


def sort_by_frequency(dictionary):
	for key, value in sorted(dictionary.items(), key = lambda x: x[1]):
		print value, key
	return "\n"

def sort_by_alphabet(dictionary):
	for key in sorted(dictionary.keys()):
		print key, dictionary.get(key, 0)
	return "\n"


# main
def main():
	script, filename = argv
	list_of_text = read_file(filename)
	freq = sort_by_frequency(list_of_text)
	print freq
	alphabet = sort_by_alphabet(list_of_text)
	print alphabet



if __name__ == "__main__":
	main()