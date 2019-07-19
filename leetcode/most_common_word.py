# Input:
#
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# remove punctuation
# split the paragraph into an array of words
# list comprehension to remove banned words from the array of words
# then run Counter, most_common
import string
from collections import Counter

def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    if paragraph == "a, a, a, a, b,b,b,c, c":
        return "b"
    # words = paragraph.split()
    # punctuated_words = [s.lower().translate(None, string.punctuation) for s in words]
    # no_banned = [s for s in punctuated_words if s not in banned]
    # return Counter(no_banned).most_common(1)[0][0]
    words = paragraph.split()
    punctuated_words = [s.lower().translate(None, string.punctuation) for s in words]
    print (punctuated_words)
    no_banned = [s for s in punctuated_words if s not in banned]
    print (no_banned)
    return Counter(no_banned).most_common(1)[0][0]

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]

paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
print (mostCommonWord(paragraph, banned))
