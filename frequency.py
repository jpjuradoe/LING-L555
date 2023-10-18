import sys

vocab = {} # dict to store frequency list

#for each of the lines of input
for line in sys.stdin.readlines():
	line = line.strip('\n') #strip any excess newlines
	if '\t' not in line: #if there is no '\t' skip the line
		continue
	row = line.split('\t') #make a list of the cells in the row
	if len(row) != 10:
		continue
	form = row[1] # the form is the valued of the 2nd cell
	if form not in vocab: #to set the freq count to 0
		vocab[form] = 0
	vocab[form] = vocab[form] + 1

#for w in vocab: #print out the freq list
#	print('%d\t%s' % (vocab[w], w))

freq = []

for w in vocab:
	freq. append((vocab[w], w))
	freq.sort(reverse=True)
print(freq[0:4])

fd = open('freq.txt', 'w+')
# For each of the items in the frequency list 
for (f, w) in freq:
    # Write out the freq and the word to the file separated by tab
    fd.write('%d\t%s\n' % (f, w))

fd.close() # Close the file

