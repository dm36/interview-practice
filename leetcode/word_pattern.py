# pattern = "abba" str = "dog cat cat dog"

# should be equal # of letters and words if not
# return False

# split the str by whitespace (to count words)

# iterate char by char in pattern and word by word in str
# see char a -> map it to the word dog
# see char b -> map it to the word cat
# next time we observe a b- we hash b in our mapping
# and expect to see the word cat
# next time we observe an a- we hash a in our mapping
# and expect to see the word dog

# def wordPattern(pattern, str):
#     arr = str.split()
#     if len(pattern) != len(arr):
#         return False
#     char_to_word = {}
#
#     for i in range(len(pattern)):
#         # if we observe a new character-
#         # and we already have a character that's mapped to the same word
#         # that's a problem
#
#         # check to see if the word is already in the values
#         # and then check to see if the character is not in keys
#         if arr[i] in char_to_word.values():
#             if pattern[i] not in char_to_word.keys():
#                 return False
#
#         if pattern[i] in char_to_word:
#             if char_to_word[pattern[i]] != arr[i]:
#                 return False
#         else:
#             char_to_word[pattern[i]] = arr[i]
#     print char_to_word
#     return True

def wordPattern(pattern, str):
    s = pattern
    t = str.split()
    print map(s.find, s)
    print map(t.index, t)

    return map(s.find, s) == map(t.index, t)
# Improved version also from there:
#
# def wordPattern(self, pattern, str):
#     f = lambda s: map({}.setdefault, s, range(len(s)))
#     return f(pattern) == f(str.split())
# From here:
#
def wordPattern(pattern, str):
    s = pattern
    t = str.split()
    print set(zip(s, t))
    print set(s)
    print set(t)

    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

print (wordPattern("abba", "dog cat cat dog"))
print (wordPattern("abba", "dog cat cat fish"))
print (wordPattern("aaaa", "dog cat cat dog"))
print (wordPattern("abba", "dog dog dog dog"))
