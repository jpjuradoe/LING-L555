#import sys

#a = 0 

#for c in sys.stdin.read():
#	print(c, file=sys,stderr)
#		a = a + 1
#print(a)

import sys
line = sys.stdin.read()
list = line.replace(" ", "\n")
#print(list)
token = list #variable to count the number of tokens
for c in list:
#       if c in ' '
        print(token, c, file=sys.stderr)
        token = token + 1
#str = sys.stdin.read()
#lista = [[" ", "\n"], [".", " ."], [",", " ,"], [":", " :"], [";", " ;"],["-", " - "],["(", " ( "], [>
#for punctuation, space in lista:
#       str = str.replace(punctuation, space)

