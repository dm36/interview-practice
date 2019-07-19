def lengthOfLongestSubstring(s):
    n = len(s)
    my_set = set()

    ans, i, j = 0, 0, 0

    # as long as i and j are less than n
    while i < n and j < n:
        # if the character at the upper bound
        # is not in the set, add it to the set
        # increment the upper bound, and update
        # the ans
        if s[j] not in my_set:
            my_set.add(s[j])
            j += 1
            ans = max(ans, j - i)

        # otherwise remove the character
        # at the s[i] location- and increment
        # the lower bound
        else:
            my_set.remove(s[i])
            i += 1

    return ans

print lengthOfLongestSubstring("abcabcbb")
