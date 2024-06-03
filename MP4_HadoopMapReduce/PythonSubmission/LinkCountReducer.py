#!/usr/bin/env python3
import sys

#TODO
parent_cnt = {}

for line in sys.stdin:
  # TODO
  parent, child = line.split()
  if parent != child:
    if child not in parent_cnt:
        parent_cnt[child] = 1
    else:
        parent_cnt[child] += 1

#TODO
for link, cnt in parent_cnt.items():
    print('%s\t%s' % (link, cnt))
