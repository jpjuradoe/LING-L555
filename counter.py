#to count a character
import sys

counter = 0

for c in sys.stdin.read():
	if c == 'o':
		counter = counter + 1

print(counter)

#To count vowels
import sys

counter = 0

for c in sys.stdin.read():
        if c in 'aeiou':
                counter = counter + 1
print(counter)
