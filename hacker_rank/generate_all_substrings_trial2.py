from collections import defaultdict
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def sherlockAndAnagrams(s):
    sub_hash = defaultdict(int)
    subs = []
    count = 0
    string_len = len(s)

    for sub_len in range(1, string_len + 1, 1):
        for i in range(string_len - sub_len + 1):
            substring = s[i : i + sub_len]
            substring = ''.join(sorted(substring))
            sub_hash[substring] += 1

    for sub_count in sub_hash.values():
        if sub_count != 1:
            count += ncr(sub_count, 2)
    print count

sherlockAndAnagrams("abba")
sherlockAndAnagrams("abcd")
sherlockAndAnagrams("ifailuhkqq")
sherlockAndAnagrams("kkkk")
sherlockAndAnagrams("cdcd")
