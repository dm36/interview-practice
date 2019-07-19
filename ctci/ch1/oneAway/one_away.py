from collections import Counter

def one_away_insert(str1, str2):
    ind1 = 0
    ind2 = 0

    # iterate until you reach the end of one string
    while (ind1 < len(str1) and ind2 < len(str2)):
        # if the characters are not equal advance the longer
        # of the two strings. if they're not equal twice and the indices
        # are different- i.e. we've been here before- return False

        # pale, ple
        #  |     |
        # when we're in the above case- we would advance the index in the first
        # string to l (the longer of the two) such that they're both at l
        if str1[ind1] != str2[ind2]:
            if ind1 != ind2:
                return False
            ind1 += 1

        # if the two characters are equal advance both strings
        else:
            ind1 += 1
            ind2 += 1

    return True

# def one_away(str1, str2):
#     # if the two strings are equal make sure that there's only one char difference
#     # in their character freq maps
#     if len(str1) == len(str2):
#         print Counter(str1)
#         print Counter(str2)
#         print Counter(str1) - Counter(str2)
#         return True if len(Counter(str1) - Counter(str2)) == 1 else False
#     # always pass the longest string first
#     if len(str1) + 1 == len(str2):
#         return one_away_insert(str2, str2)
#     if len(str1) == len(str2) + 1:
#         return one_away_insert(str1, str2)
#     # if the strings aren't equal in length or one length apart- can't possibly
#     # be one away
#     else:
#         return False

# Find the number of characters that differ between the two
# strings and return True if that # is equal to 1
def one_away(str1, str2):
    # Frequency map for the differing chars of the two
    # strings
    if len(str1) > len(str2):
        diff_counter = Counter(str1) - Counter(str2)
    else:
        diff_counter = Counter(str2) - Counter(str1)
    print diff_counter

    # Return whether the # of differing chars is equal to 1
    return sum(diff_counter.values()) == 1

print one_away("paale", "ple")
print one_away("ple", "paale")
print one_away("pale", "ple")
print one_away("pales", "pale")
print one_away("pale", "bale")
print one_away("pale", "bae")
