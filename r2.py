import sys

freq = [] #declare a new list

fd = open('fq2.txt', 'r') # open the file in read mode

for line in fd.readlines(): #for each of the lines in the file
	line = line.strip('\n') #strip the newline
	(f, w) = line.split('\t') #split the line on \t and put the resulting 2 values in a tuple
	freq.append((int(f), w))

rank = 1 #highest rank
min = freq[0][0] # the current minimum
ranks = [] #list of ranks

for i in range(0, len(freq)): #for each index in the list [0,1,2..., len()]
	if freq[i][0] < min: #if freq lower than the minimum
		rank = rank + 1
		min = freq[i][0] #set the minimum
	ranks.append((rank, freq[i][0], freq[i][1])) #add a 3-tuple of rank
for c in ranks:
	print(c)
