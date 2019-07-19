# https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/

def generate_all_substrings(my_string):
    substrings = []
    for size in range(len(my_string), 0, -1):
        for start_ind in range(len(my_string)):
            if start_ind + size > len(my_string):
                break
            substrings.append(my_string[start_ind:start_ind + size])
    return substrings

def lengthOfLongestSubstring(my_string):
    substrings = generate_all_substrings(my_string)
    for sub in substrings:
        if len(sub) == len(set(sub)):
            return len(sub)

# def lengthOfLongestSubstring(self, s):
#     dct = {}
#     max_so_far = curr_max = start = 0
#     for index, i in enumerate(s):
#         if i in dct and dct[i] >= start:
#             max_so_far = max(max_so_far, curr_max)
#             curr_max = index - dct[i]
#             start = dct[i] + 1
#         else:
#             curr_max += 1
#         dct[i] = index
#     return max(max_so_far, curr_max)

 # d = ""
 #        f = ""
 #        for i in range(len(s)):
 #            if s[i] not in f:
 #                f += s[i]
 #            else:
 #                if len(d) < len(f):
 #                    d = f
 #                f = f[f.index(s[i])+1::] + s[i]
 #
 #        return max(len(d), len(f))
print lengthOfLongestSubstring("abcabcbb")
