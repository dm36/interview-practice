# All permutations of a string with the same length as the original string

# Take a string "abc":
# Take away a character- say a- so that we now have the string "bc"
# Form all permutations of bc ["bc", "cb"] (recursively)
# For each permutation of bc, concatenate a at every possible spot in the string, so for bc:
# ["abc", "bac", "bca"]
# Same idea for cb, concatenate a at every spot:
# ["acb", "cab", "cba"]

# Say we took the character b away instead so that we now had the string "ac"
# All permutations of ac ["ac", "ca"]
# For each permutation of ac, concatenate b at every spot in the string so for ac:
# ["bac", "abc", "acb"]
# Same idea for ca, concatenate b at every spot
# ["bca", "cba", "cab"]

# So technically we'd only have to do this process once.

def permutation(str):
    if len(str) == 1:
        return str

    char = str[0]
    remainder = str[1:]

    remainder_perms = permutation(remainder)

    perms = []
    for perm in remainder_perms:
        # +1 to handle "bc" + "a" or "bca"
        # for the above example- i would be 2, perms[:i] would be "bc",
        # char would be a and perm[i:] would be the "" (empty string)

        # if perm was "c" and char was "b":
        # first loop i would be 0, perm[:i] would be "", char would be
        # b and perm[i:] would be "c" so "bc"
        # second loop i would be 1, perm[:i] would be c, char would be b
        # and perm[i:] would be "" so "cb"
        for i in range(len(perm)+1):
            perms.append(perm[:i] + char + perm[i:])

        # if len(perm) == 1:
        #     perms.append(perm + char)
        #     perms.append(char + perm)
        # else:
        #     for i in range(len(perm)):
        #         perms.append(perm[:i] + char + perm[i:])
        #     perms.append(perm + char)
    return perms

# itertools implementation
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210

    # tuple of iterable so "abc" -> ("a", "b", "c")
    pool = tuple(iterable)

    # 3 in this case
    n = len(pool)

    # also 3 in this case
    r = n if r is None else r
    if r > n:
        return

    # indices would be [0, 1, 2]
    indices = range(n)

    # indices in reverse? [2, 1, 0]
    cycles = range(n, n-r, -1)

    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

# another itertools implementation
# def permutations(iterable, r=None):
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     for indices in product(range(n), repeat=r):
#         if len(set(indices)) == r:
#             yield tuple(pool[i] for i in indices)

print permutation("abc")
print len(permutation("cats"))
for perm in permutations("abc"):
    print perm
