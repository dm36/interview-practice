def abbreviate(s):
    arr = s.split('-')
    final = []
    for word in arr:
        if len(word) < 4:
            final.append(word)
        else:
            final.append(word[0] + str(len(word) - 2) + word[-1])
    return '-'.join(final)


print abbreviate("internationalization")

print abbreviate("elephant-ride")
