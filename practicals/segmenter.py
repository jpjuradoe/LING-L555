#To replace every '. ' with a full stop and a newline character  '\n\'

import sys

line = sys.stdin.readline()

while line:
	line = line.replace('.', '.\n')
	print(line)
	line = sys.stdin.readline()
