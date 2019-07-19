# https://www.hackerrank.com/domains/algorithms

def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    for i in range(len(s)):
        str = s[:i] + s[i+1:]
        if str == str[::-1]:
            return i
    return -1


print palindromeIndex("bcbc")
print palindromeIndex("aaab")
print palindromeIndex("baa")
print palindromeIndex("aaa")
