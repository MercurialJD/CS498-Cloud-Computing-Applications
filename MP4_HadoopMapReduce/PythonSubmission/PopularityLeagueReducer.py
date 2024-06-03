#!/usr/bin/env python3
import sys

#TODO
def sort_schema(x):
    return x[0]

link_cnt_map, counts = [], []
for line in sys.stdin:
    # TODO
    link, cnt = line.split()
    link_cnt_map.append((int(link), int(cnt)))
    counts.append(int(cnt))

link_cnt_map.sort(key=sort_schema, reverse=True)
counts.sort()

#TODO
for link, cnt in link_cnt_map:
    print('%s\t%s' % (link, counts.index(cnt)))