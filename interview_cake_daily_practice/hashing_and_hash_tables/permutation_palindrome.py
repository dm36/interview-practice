# string is a permutation of a palindrome if it has at most one character
# with an odd frequency
from collections import Counter
def has_palindrome_permutation(the_string):
    counter = Counter(the_string)
    return len([freq for freq in counter.values() if freq % 2 == 1]) <= 1

# if the character is already in unpaired_characters remove it
# if the character is not in unpaired_characters we add it
def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutatiosn if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1

result = has_palindrome_permutation('aabcbcd')
print result
