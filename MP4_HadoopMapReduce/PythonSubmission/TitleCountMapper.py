#!/usr/bin/env python3
import sys
import string

def tokenize(text: str, delimiters: list):
    for d in delimiters:
        text = text.replace(d, ' ')

    return text

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

stop_words, delimiters = [], []

# TODO
with open(stopWordsPath) as f:
    for line in f:
        stop_words.append(line.strip())

#TODO 
with open(delimitersPath) as f:
    chars = f.read().rstrip('\n')
    for c in chars:
        delimiters.append(c)

# print(stop_words)
# print(delimiters)

for line in sys.stdin:
    # TODO
    words = tokenize(line, delimiters).lower().split()
    for word in words:
        if word not in stop_words:
            print('%s\t%s' % (word, str(1)))
