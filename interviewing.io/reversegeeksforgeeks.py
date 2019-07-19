# Python3 program to reverse a string
# s = input()
s = "i like this program very much"

# List of characters format seen on interviewing.io
arr = []
for i in range(len(s)):
    arr.append(s[i])
print arr

# Convert list of characters back to a string
str = ""
for i in range(len(arr)):
    str += arr[i]
print str

# List of words
words = str.split(' ')
print words

# Reverse list of words by inserting each word to the front
# of a new array
string = []
for word in words:
    string.insert(0, word)
print string

# Join the list with whitespace
print("Reversed String:")
print(" ".join(string))
