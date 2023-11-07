freq = []
for i in freq:
    palindrome = False
    rev = ''

    # If the length of the word is 1, skip to the next word
    if len(i[1]) == 1:
        continue

    # Generate a sequence of numbers from 1 to the length
    for j in range(1, len(i[1]) + 1):
        # Build up a reversed version of the word
        # by adding characters from the end of it
        rev = rev + i[1][-j]

    if i[1] == rev:
        palindrome = True

    if palindrome:
        print('%d\t%s' % (i[0], i[1]))


"""
import sys

freq = []

f = open('freq.txt', 'r')

#for line in f.read():
for i in f.freq:
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
"""
"""
freq = []

f = open('freq.txt', 'r')

for line in f.read():
	def is_palindrome(s):
		rev = ''
		if len(s) == 1:
			return False
		for j in range(1, len(s) + 1):
			rev = rev + s[-j]
		if s == rev:
			return True
		return False
	for i in freq:
		if is_palindrome(i[1]):
			print('%d\t%s' % (i[0], i[1]))
"""
