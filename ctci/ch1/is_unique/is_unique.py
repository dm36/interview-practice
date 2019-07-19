# O(n)
def is_unique(string):
    freq_map = {}
    for i in range(len(string)):
        if string[i] not in freq_map:
            freq_map[string[i]] = 1
        else:
            return False
    return True

# O(n log n)
def is_unique_sort(string):
    string = ''.join(sorted(string))
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            return False
    return True

# O (n^2)
def is_unique_compare(string):
    for i in range(len(string)):
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
                return False
    return True


print "Is unique: "
print is_unique("swag")
print is_unique("swags")
print is_unique("dogd")
print

print "Is unique sort: "
print is_unique_sort("swag")
print is_unique_sort("swags")
print is_unique_sort("dogd")
print

print "Is unique compare: "
print is_unique_compare("swag")
print is_unique_compare("swags")
print is_unique_compare("dogd")
