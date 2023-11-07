def is_palindrome(s):
	rev = ''
	if len(s) == 1:
		return False
	for j in range(1, len(s) + 1):
		rev = rev + s[-j]
	if s == rev:
		return True
	return False

freq = []

#f = open('f2.txt', 'r')

#for line in f.readlines():
with open('más.txt', 'r') as f:
	for line in f:
		parts = line.strip().split('\t')
		if len(parts) != 2:
#			print(f"Skipping line: {line}")
			continue
		frequency, word = int(parts[0]), parts[1]
		freq.append((frequency, word))
		print(f"Added: {frequency}\t{word}")
for i in freq:
	if is_palindrome(i[1]):
		print('%d\t%s' % (i[0], i[1]))
