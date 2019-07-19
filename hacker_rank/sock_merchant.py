#!/bin/python

import math
import os
import random
import re
import sys
import collections

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_map = collections.defaultdict(int)
    pairs = 0

    for sock in ar:
        sock_map[sock] += 1

    for sock_count in sock_map.values():
        pairs += sock_count / 2

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# from itertools import groupby
# n = int(raw_input())
# c = map(int, raw_input().split())
#
# ans = 0
# for val in [len(list(group)) for key, group in groupby(sorted(c))]:
#     ans = ans + val/2
# print ans
