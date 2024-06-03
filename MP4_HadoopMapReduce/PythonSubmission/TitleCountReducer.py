#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
counter = {}

for line in sys.stdin:
    # TODO
    word, cnt = line.split()
    if word not in counter:
        counter[word] = int(cnt)
    else:
        counter[word] += int(cnt)

# TODO
for word, cnt in counter.items():
    print('%s\t%s' % (word, str(cnt)))
