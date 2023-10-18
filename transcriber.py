import sys

IPA = {}

misc = open('IPA.txt', 'r')

for line in misc.readlines():
	line = line.strip('\n')
	(f, w) = line.split('\t')
	IPA[f] = w

for line in sys.stdin.readlines():
	line = line.strip('\n')
	if '\t' not in line:
		print(line)
	if '\t' in line:
		row = line.split('\t')
		form = row[1]
		transcription = form
		for character in IPA:
				transcription = transcription.replace(character, IPA[character])
		row[9] = 'IPA=' + transcription
		print('\t'.join(row)) 
