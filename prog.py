"""
import sys

a = 0 # This is a variable for counter the number of vowels

for c in sys.stdin.read():
	print('Main loop:', a, c, file=sys.stderr)
	if c.lower() in 'aeiouáéíóúäëïöüâêîôûàèìòù':
		print('Found a vowel!', c, file=sys.stderr)
		a = a + 1

print(a)
"""
import sys

a = 0 # This is a variable for counter the number of vowels

for c in sys.stdin.read():
        print(a, c, file=sys.stderr)
#        if c.lower() in 'aeiouáéíóúäëïöüâêîôûàèìòù':
#		print(c, file=sys.stderr)
        a = a + 1
print(a)

