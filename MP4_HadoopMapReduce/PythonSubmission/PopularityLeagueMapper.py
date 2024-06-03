#!/usr/bin/env python3
import sys

leaguePath = sys.argv[1]

#TODO
league = []
with open(leaguePath) as f:
       for line in f:
              league.append(int(line))

for line in sys.stdin:
       #TODO
       link, cnt = line.split()
       if int(link) in league:
              print('%s\t%s' % (link, cnt))
