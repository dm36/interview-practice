# aba
# 10
# abaabaabaa

# abcac
# 10
# abcacabcac

# count the number of a's in s- call this count
# n / len(s) * count
# check # of a's in s in its first (n % len(s) chars
# add these two!

# so to take an example:
# aba- count would be 2
# 10 / 3 * 2 so 6
# 3 % 2  = 1 so we check the first 1 char of "abc" and count the # of a's
def repeatedString(s, n):
    s_count = 0
    for char in s:
        if char == 'a':
            s_count += 1

    final_count = (n / len(s)) * s_count

    mod = n % len(s)

    for i in range(mod):
        if s[i] == 'a':
            final_count += 1
    return final_count

# print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

repeatedString("aba", 10)
