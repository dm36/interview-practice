# if the strings are the same => check to see
# if there are any more than two differing characters

# if one string is longer than the other =>
# pass the longer string in the second position

# if two characters differ -> increment the index
# of the longer string, if two characters differ
# and the indices are different return False

def one_edit_distance_replace(str1, str2):
    flag = False
    for i in range(len(str1)):
        if flag and str1[i] != str2[i]:
            return False
        if str1[i] != str2[i]:
            flag = True
    return True

def one_edit_distance_insert(string1, string2):
    i, j = 0, 0

    while i < len(string1) and j < len(string2):
        if string1[i] == string2[j]:
            i += 1
            j += 1
        elif string1[i] != string2[j]:
            j += 1
        elif string1[i] != string2[j] and i != j:
            return False
    return True

def one_edit_distance(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False
    if len(string1) == len(string2) + 1:
        return one_edit_distance_insert(string2, string1)
    elif len(string2) == len(string1) + 1:
        return one_edit_distance_insert(string1, string2)
    elif len(string1) == len(string2):
        return one_edit_distance_replace(string1, string2)

print one_edit_distance("abcde", "abxde")
print one_edit_distance("abcde", "abcxde")
print one_edit_distance("abcde", "abcdex")
