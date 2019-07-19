# determine if two strings share a common substring

def all_substrings(s1):
    arr_of_substrings = []
    for i in range(len(s1)):
        for j in range(len(s1)):
            arr_of_substrings.append(s1[i:i+j])
    print arr_of_substrings

def twoStrings(s1, s2):
    if len(set(s1).intersection(set(s2))) > 0:
        return True
    else:
        return False

print twoStrings("hello", "world")
