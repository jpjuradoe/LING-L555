import sys

vocab = {}
for line in sys.stdin.readlines():
	line = line.strip('\n')
	if '\t' not in line:
		continue
	row = line.split('\t')
	if len(row) != 10:
		continue
	form = row[1]
	if form not in vocab:
		vocab[form] = 0
	vocab[form] = vocab[form] + 1
for w in vocab:
	print('%d\t%s' % (vocab[w], w))

freq = []

for w in vocab:
	freq.append((vocab[w], w))
	freq.sort(reverse=True)
print(freq[0:4])
fd = open('c-syll.txt', 'w+')
for (f, w) in freq:
    fd.write('%d\t%s\n' % (f, w))
fd.close()
