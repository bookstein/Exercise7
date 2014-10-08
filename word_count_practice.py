""" This is a practice redo of Exercise 7 from Monday 10/6.
Working on it on Tuesday 10/7.
How long does it take me to complete the exercise?"""

from sys import argv
import string

script, filename = argv

def count_words(filename):
	f = open(filename)

	for line in f:
		line = line.rstrip()
		textstring = line.split()
		if string.punctuation in textstring:
			# remove punctuation

