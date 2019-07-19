def reverse_words(message):
    message.reverse()
    i = 0

    # i iterates over the length of the message
    # j iterates from i to the length of the message + 1 until it arrives
    # at either a whitespace or the length of the message (range(i), len(message) + 1)
    # we then reverse up to that point and then increment i to be 1 past j

    # ['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']
    # ['l', 'a', 'e', 't', 's', ' ', 'd', 'n', 'u', 'o', 'p', ' ', 'e', 'k', 'a', 'c']
    # i = 0, j = 5
    # ['s', 't', 'e', 'a', 'l', ' ', 'd', 'n', 'u', 'o', 'p', ' ', 'e', 'k', 'a', 'c']
    # i = 6, j = 11
    # ['s', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 'e', 'k', 'a', 'c']
    # i = 12, j = 15
    # ['s', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 'c', 'k', 'a', 'c']

    # so the reason j iterates to len(message) + 1 is so that it goes up to the length of
    # the message- and that way we can use j - 1 in our helper function call for both the
    # whitespace and the end of message case

    while i < len(message):
        for j in range(i, len(message) + 1):
            if j == len(message) or message[j] == ' ':
                reverse_helper(message, i, j - 1)
                i = j + 1
    return message

def reverse_helper(message, i, j):
    ind1 = i
    ind2 = j
    while ind1 < ind2:
        message[ind1], message[ind2] = message[ind2], message[ind1]
        ind1 += 1
        ind2 -= 1

message = ['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']

print reverse_words(message)

# Prints: 'steal pound cake'
# print(''.join(message))
