import sys

freq = []

fd = open('IPA.txt', 'w+')

fd = open('freq.txt', 'r')
# For each of the lines in the file
for line in fd.readlines():
    # Strip the newline
    line = line.strip('\n')
    # Split the line on the tab character and put the 
    # resulting two values in a tuple
    (f, w) = line.split('\t')
    # Append the tuple to the list
    freq.append((int(f), w))

