#To count: lines, tokens, and characters

import sys

tcounter = 0; chcounter = 0; lcounter = 0; vcounter = 0; ccounter = 0; sycounter = 0;

#Variable for all.
for c in sys.stdin.read():

#To count characters. No 'if' statement needed.
	sys.stdout.write(c)
	chcounter = chcounter + 1

#To count tokens by counting the number of spaces +1 (last word).
	if c in ' ':
		tcounter = tcounter + 1

#To count lines:
	if c in '\n':
		lcounter = lcounter + 1

#To count all the tokens including '\n' and '.'
#tcounter = tcounter + lcounter

	if c.lower() in 'aeiouáéíóúäëïöüàèìòùâêîôû':
		vcounter = vcounter + 1

	if c.lower() in 'bcdfghjklmnñpqrstvwxyz':
		ccounter = ccounter + 1

tcounter = tcounter + lcounter
sycounter = vcounter / tcounter

print("Number of characters =", chcounter)
print("Number of tokens =", tcounter)
print("Number of lines =", lcounter)
print("Number of consonants =", ccounter)
print("Number of vowels =", vcounter)
print("Average number of syllables per word =", sycounter)

