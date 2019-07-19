# Outer loop i takes all possible substring lengths
# Inner loop j- sliding window- make sure not to go past the length of the string!

# sorted returns an array of sorted chars
# ''.join returns a string where the array of sorted chars
# are joined by ''

def is_unique(s):
    sorted_sub = ''.join(sorted(s))
    for i in range(1, len(sorted_sub)):
        if sorted_sub[i-1] == sorted_sub[i]:
            return False
    return True

def gen_all_substrings(s):
    for i in range(len(s), -1, -1):
        for j in range(len(s) - i + 1):
            if is_unique(s[j:j+i]):
                print s[j:j+i]
                return len(s[j:j+i])

print gen_all_substrings("pwwkew")
