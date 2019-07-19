from collections import defaultdict

# Frequency map of characters (all converted to lower-case)
# disregarding whitespace. Can only have at most one odd frequency
# for the string to be a palindrome
def palindrome_permutation(x):
    freq_map = defaultdict(int)
    odd_count = 0

    for i in range(len(x)):
        if x[i] == ' ':
            continue
        freq_map[x[i].lower()] += 1

    for vals in freq_map.values():
        if vals % 2 == 1:
            odd_count += 1
        if odd_count > 1:
            return False
    return True

def palindrome_permutation_compact(x):
    freq_map = defaultdict(int)
    odd_count = 0

    for i in range(len(x)):
        if x[i] == ' ':
            continue

        freq_map[x[i].lower()] += 1
        if freq_map[x[i].lower()] % 2 == 1:
            odd_count += 1
        else:
            odd_count -= 1

    if odd_count == 0 or odd_count == 1:
        return True
    else:
        return False

print palindrome_permutation("Tact Coa")
print palindrome_permutation("tactcoapapa")

print palindrome_permutation_compact("Tact Coa")
print palindrome_permutation_compact("tactcoapapa")
