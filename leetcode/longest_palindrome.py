# Outer loop i takes all possible substring lengths
# Inner loop j- sliding window- make sure not to go past the length of the string!

# sorted returns an array of sorted chars
# ''.join returns a string where the array of sorted chars
# are joined by ''

def is_palindrome(s):
    return s == s[::-1]

def longestPalindrome(s):
    for i in range(len(s), -1, -1):
        for j in range(len(s) - i + 1):
            if is_palindrome(s[j:j+i]):
                print s[j:j+i]
                return len(s[j:j+i])

print longestPalindrome("cbbd")
