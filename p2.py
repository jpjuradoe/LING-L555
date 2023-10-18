import sys

freq = []

f = open('freq.txt', 'r')

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
