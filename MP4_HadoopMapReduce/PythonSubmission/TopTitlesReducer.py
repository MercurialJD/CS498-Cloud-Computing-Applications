#!/usr/bin/env python3
import sys

def sort_schema(x):
    return int(x[1]), x[0]

# TODO
words_freqs = []

for line in sys.stdin:
    #TODO
    words_freqs.append(line.split())
# print(words_freqs)

#TODO
words_freqs.sort(key=sort_schema)
for word, freq in words_freqs[-10:]:
    print('%s\t%s' % (word, freq))
