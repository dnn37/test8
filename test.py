author__ = 'DELL'
print('hello world. I love you!\n')
import sys
for line in sys.stdin:
    for token in line.strip().split():
        print(token + '\t1')
