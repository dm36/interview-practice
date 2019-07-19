def reverseWords(str):
    reversed_str = str[::-1]
    arr = reversed_str.split()
    arr.reverse()
    print ' '.join(arr)

# split the string into an array based on whitespace
# so ['Let's', 'take', 'LeetCode', 'contest']
# reverse each string in the array and then join
# with whitespace
def reverseWords(self, s):
    return ' '.join(x[::-1] for x in s.split())

# Split the string based on whitespace, reverse the
# array, join with whitespace and then reverse the
# result
def reverseWords(self, s):
    return ' '.join(s.split()[::-1])[::-1]


s = "Let's take LeetCode contest"
reverseWords(s)
