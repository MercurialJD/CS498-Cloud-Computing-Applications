#!/usr/bin/env python3
import sys
import math

def mean(nums):
    return math.floor( sum(nums) / len(nums) )

def var(nums):
    mu = mean(nums)
    squared_diffs = [(n - mu) ** 2 for n in nums]
    return math.floor(sum(squared_diffs) / len(nums))

nums = []

for line in sys.stdin:
    # TODO
    nums.append(int(line))

#TODO
print('%s\t%d' % ("Mean", mean(nums)))
print('%s\t%d' % ("Sum", sum(nums)))
print('%s\t%d' % ("Min", min(nums)))
print('%s\t%d' % ("Max", max(nums)))
print('%s\t%d' % ("Var", var(nums)))
