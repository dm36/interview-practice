def alternatingCharacters(s):
    char_count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            char_count += 1
    return char_count

print alternatingCharacters("AAAA")
print alternatingCharacters("BBBBB")
