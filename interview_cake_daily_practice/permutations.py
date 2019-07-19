# permutations of dog:

# all permutations of do with g inserted at every possible
# position in each of those permutations

# permutations of "do"- "do", "od"

# inserting "g" in "do"
# "gdo", "dgo", "dog"

# inserting "g" in "od"
# "god", "ogd", "odg"

def permutations(str):
    if len(str) == 0 or len(str) == 1:
        return str

    char = str[-1]
    sub_str = str[:-1]

    sub_perms = permutations(sub_str)
    perms_array = []
    for perm in sub_perms:
        for i in range(len(perm) + 1):
            final_str = perm[:i] + char + perm[i:]
            perms_array.append(final_str)
    return perms_array

# str1 = "g"
# str2 = "do"

# when i = 0
# "" + "g" + "do"

# when i = 1
# "d" + "g" + "o"

# when i = 2
# "do" + "g" + ""

# for i in range(len(str2)+1):
#     final_str = str2[:i] + str1 + str2[i:]

print permutations("dog")
print permutations("cat")
