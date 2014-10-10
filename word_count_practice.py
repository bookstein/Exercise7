""" This is a practice redo of Exercise 7 from Monday 10/6.
Working on it on Friday 10/10.
How long does it take me to complete the exercise?"""

import string
from sys import argv
# open and read in file -- no need to do it line by line
# lowercase, punctuation, line split

def read_file(filename):
	f = open(filename)
	text = f.read()
	text = text.lower()
	words_list = text.split()
	# for word in words_list:
	# 	for punc in string.punctuation:
	# 		if punc in word:
				# //remove punctuation

	print words_list




# create dictionary of all words



# loop through dictionary and count


# main
def main():
	script, filename = argv
	read_file(filename)
	# make_dict()
	# count_words()



if __name__ == "__main__":
	main()