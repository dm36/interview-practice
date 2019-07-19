from collections import Counter

def anagrams(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    return False

def anagrams(string1, string2):
    if Counter(string1) == Counter(string2):
        return True
    return False

print anagrams('rail safety', 'fairy tales')
print anagrams('Hi there', 'Bye there')
