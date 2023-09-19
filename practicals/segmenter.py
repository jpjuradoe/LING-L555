#To replace every '. ' with a full stop and a newline character '\n'.

import sys

line = sys.stdin.read()

seg = line.replace(". ", ".\n")

print(seg)

