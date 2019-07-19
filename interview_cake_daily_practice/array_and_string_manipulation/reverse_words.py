# first reverse the message- but after reversing the message the words are now reversed
# too- so you identify each word's end- and reverse those words too
def reverse_words(message):
    message.reverse()
    print message
    i = 0

    # i iterates through the length of the message, j starts from i
    # and looks for either a whitespace or the end of the message.
    # when we find either of those two things- we save away the indices
    # don't think we can just pass i and j because our function will
    # change these indices- and pass this to our helper function
    # to reverse the string

    # make sure to break- so that the program repeats the process- sets
    # i to j + 1 so that we start after the whitespace following the
    # word we just reversed- and once again go searching for the end of the
    # word before we reverse it
    while i < len(message):
        for j in range(i, len(message) + 1):
            if j == len(message) or message[j] == ' ':
                print j
                start_ind, end_ind = i, j - 1
                print start_ind, end_ind
                reverse_string(message, start_ind, end_ind)
                print message
                break
        i = j + 1
    print message

def reverse_string(arr_of_chars, i, j):
    while i < j:
        arr_of_chars[i], arr_of_chars[j] = arr_of_chars[j], arr_of_chars[i]
        i += 1
        j -= 1


message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))
