# time complexity is O(n^2)
# space complexity is # of substrings which is also O(n^2)
# no of substrings of length 1 is n, 2 is n-1, 3 is n-2 so
# n + n-1 + n-2... = O(n^2)
# link here: https://www.geeksforgeeks.org/number-substrings-string/:

# sub_len takes on all possible substring lengths and
# then we use a sliding window to obtain all substrings of length 1,
# 2, 3, etc.

def generate_all_substrings(s):
    subs = []
    string_len = len(s)
    for sub_len in range(1, string_len + 1, 1):
        for i in range(string_len - sub_len + 1):
            substring = s[i : i + sub_len]
            subs.append(substring)
    return subs

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def sherlockAndAnagrams(s):
    sub_strings = generate_all_substrings(s)
    sub_anagrams = []
    for i in range(len(sub_strings)):
        for j in range(len(sub_strings)):
            if i != j and is_anagram(sub_strings[i], sub_strings[j]):
                if (sub_strings[i], sub_strings[j]) not in sub_anagrams:
                    if (sub_strings[j], sub_strings[i]) not in sub_anagrams:
                        sub_anagrams.append((sub_strings[i], sub_strings[j]))
    print sub_anagrams
    return len(sub_anagrams)

print sherlockAndAnagrams("cdcd")
