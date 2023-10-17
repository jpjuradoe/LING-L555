import sys

a = 0
c = '.'
c = c.replace(' ', ' .')

for line in sys.stdin.readlines():
	if line.strip() == '':
		continue
	a = a + 1
	b = 0
	print('\n# sent_id = %d' % (a))
	print('# text = %s' % (line))
	line = line.replace('.', ' . ')
	line = line.replace(',', ' , ')
	line = line.replace(':', ' : ')
	line = line.replace(';', ' ; ')
	line = line.replace('-', ' - ')
	line = line.replace('(', ' ( ')
	line = line.replace(')', ' ) ')
	line = line.replace('"', ' " ')
	tokens = line.split()
	for token in tokens:
		b = b + 1
		print(b, '\t', token, '\t_\t_\t_\t_\t_\t_\t_\t_')
