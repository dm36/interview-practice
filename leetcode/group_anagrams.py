# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Create buckets- i.e. an array of anagrams
# As you pass through each string in strs check if its anagram of the
# first string in each bucket- if it is add it to that bucket
# otherwise create a new one
import collections

def group_anagrams(strs):
    buckets = [[strs[0]]]
    for i in range(1, len(strs)):
        word = strs[i]
        break_flag = False
        for bucket in buckets:
            if break_flag == True:
                break
            if is_anagram(word, bucket[0]):
                bucket.append(word)
                break_flag = True
        if break_flag == False:
            buckets.append([word])
    print buckets

# Tuples of sorted characters mapped to a list of
# strings of all anagrams having those characters- return the
# list of characters
def group_anagrams_opt(strs):
    hash = collections.defaultdict(list)
    for str in strs:
        hash[tuple(sorted(str))].append(str)
    return hash.values()

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print group_anagrams_opt(["eat", "tea", "tan", "ate", "nat", "bat"])
