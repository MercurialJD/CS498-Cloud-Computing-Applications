#!/usr/bin/env python3
import sys

#TODO
has_parent = {}

for line in sys.stdin:
  # TODO
  parent, child = line.split()
  if parent != child:
    has_parent[child] = True
    if parent not in has_parent:
      has_parent[parent] = False

#TODO
orphans = set()
for link in has_parent:
  if not has_parent[link]:
    orphans.add(link)

orphans = list(orphans)
orphans.sort(key=int)

for link in orphans:
  print(link)
