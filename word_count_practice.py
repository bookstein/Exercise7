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
	words = text.split()

	for word in words:
		dictionary[word] = dictionary.get(word, 0) + 1 # increments value by 1

	print dictionary


def sort_by_frequency(dict):
	pass



# main
def main():
	script, filename = argv
	list_of_text = read_file(filename)




if __name__ == "__main__":
	main()