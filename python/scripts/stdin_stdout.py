# > who | python stdin_stdout.py
import sys

counter = 1
#while True:
    #line = sys.stdin.readline()
    #if not line:
        #break
    #print '%s: %s' % (counter, line)
    #counter += 1

for i, line in enumerate(sys.stdin):
    print '%s: %s' % (i, line)
