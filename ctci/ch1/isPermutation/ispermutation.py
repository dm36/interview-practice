# O(nlogn)
def isPermutation(string1, string2):
    # Array w/ the characters of the string sorted
    return sorted(string1) == sorted(string2)

print isPermutation("dog", "god")
print isPermutation("dogs", "god")
