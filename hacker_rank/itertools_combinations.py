# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

def printed_combinations(s, k):
    for i in range(1, k + 1):
        arr = []
        lst = list(combinations(s, i))
        for elem in lst:
            string = ''.join(elem)
            arr.append(''.join(sorted(string)))

        arr.sort()
        for elem in arr:
            print elem


s, k = raw_input().split(" ")
k = int(k)
printed_combinations(s, k)
