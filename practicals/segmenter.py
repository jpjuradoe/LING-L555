#To replace every '. ' with a full stop and a newline character  '\n\'

import sys

line = sys.stdin.readline()

lines = line.replace('.', '.\n')

while lines:
	print(lines)
	lines = sys.stdin.readline()
