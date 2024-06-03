#!/usr/bin/env python3
import sys

def sort_schema(x):
    return x[1], x[0]

parent_cnt = []
for line in sys.stdin:
    # TODO
    link, cnt = line.split()
    parent_cnt.append((int(link), int(cnt)))

parent_cnt.sort(key=sort_schema)
for link, cnt in parent_cnt[-10:]:
    print('%s\t%s' % (link, cnt))
