""" This is a practice redo of Exercise 7 from Monday 10/6.
Working on it on Friday 10/10.
How long does it take me to complete the exercise?"""

import string
from sys import argv
# open and read in file -- no need to do it line by line
# lowercase, punctuation, line split



# main
def main():
	script, filename = argv
	list_of_text = read_file(filename)
	make_dict(list_of_text)
	# count_words()



if __name__ == "__main__":
	main()