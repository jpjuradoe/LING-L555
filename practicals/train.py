import sys

x = ['#P', 'count', 'tag', 'form']
y = open('wiki.conllu', 'r')

cList = [] #counter list
tagFq = {} #tag freq
counts = {} #word-tag freq

for line in y.readlines():
	line = line.strip('\n')
	if '\t' not in line:
		continue
	row = line.split('\t')
	form = row[1]
	tag = row[3]
	cList.append((form, tag))
	if tag not in tagFq:
		tagFq[tag] = 0
	tagFq[tag] = tagFq[tag] + 1
	if form not in counts:
		counts[form] = {}
	if tag not in counts[form]:
		counts[form][tag] = 0
	counts[form][tag] += 1
print('\t'.join(x))

columnP ={} #to calculate the P value

for p, c in tagFq.items():
	average = c / sum(tagFq.values())
	columnP[p] = average

for p, average in columnP.items():
	print('%.2f' % (average), '\t', tagFq[p], '\t', p, '\t', '_')

for form in counts:
	total = 0
#	sum(i for in counts[form].values) #not working for me
	for tag in counts[form]:
		total += counts[form][tag]
	for tag in counts[form]:
		print(counts[form][tag]/total,'\t', counts[form][tag], '\t', tag, '\t', form)
