import sys

f = open('freq.txt', 'r')

freq = []

for line in f.read():
	for i in freq:
		palindrome = False
		rev = '' #if the length of the word is 1, skip to the next word
		if len(i[1]) == 1:
			continue
		for j in range(1, len(i[1]) + 1): #generate a sequence of numbers from 1 to the length
		#Build up a reversed version of the word
		#by adding characters from the end of it
			rev = rev + i[1][-j]
		if i[1] == rev:
			palindrome = True
		if palindrome:
			print('%d\t%s' % (i[0], i[1]))
