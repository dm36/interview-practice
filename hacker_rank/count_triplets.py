from itertools import combinations

def count_triplets(arr, r):
    combs = []
    count = 0
    # Combinations of the above arr of length 3
    for c in combinations(arr, 3):
        for i in range(1, len(c)):
            if c[i] != c[i-1] * r:
                break
            if i == len(c) - 1:
                count += 1
    print count


# Array of tuples of each element and its corresponding index
# (index first)
# ind_elem = []
# for ind, val in enumerate(arr):
#     ind_elem.append((ind, val))

count_triplets([1, 4, 16, 64], 4)
