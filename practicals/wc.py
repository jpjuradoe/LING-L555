#To count: lines, tokens, characters, vowels, consonants, and syllables

import sys

tcounter = 0; chcounter = 0; lcounter = 0; vcounter = 0; ccounter = 0; sycounter = 0;

for c in sys.stdin.read(): #Variable for all.
	sys.stdout.write(c) #To count characters. No 'if' statement needed.
 	chcounter = chcounter + 1
	if c in ' ': #To count tokens by counting the number of spaces +1 (last word).
		tcounter = tcounter + 1
	if c in '\n': #To count lines:
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
