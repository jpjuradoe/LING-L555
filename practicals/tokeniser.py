import sys

str = sys.stdin.read()

lista = [[" ", "\n"], [".", " ."], [",", " ,"], [":", " :"], [";", " ;"],["-", " - "],["(", " ( "], [")", " ) "]]

for punctuation, space in lista:
	str = str.replace(punctuation, space)

print(str)
