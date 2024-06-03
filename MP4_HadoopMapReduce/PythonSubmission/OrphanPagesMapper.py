#!/usr/bin/env python3
import sys

for line in sys.stdin:
  # TODO
  parent, children = line.strip().split(': ')

  for child in children.split():
    print('%s\t%s' % (parent, child))
