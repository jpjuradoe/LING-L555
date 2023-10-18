#Print text in a line
"""
import sys

text = sys.stdin.read()

for c in text:
	print(c)

"""
"""
import sys

for c in sys.stdin.read():
	print(c)

"""
#Print text in the same line
import sys

for c in sys.stdin.read():
	sys.stdout.write(c)
