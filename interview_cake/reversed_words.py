# idea is to reverse the array of chars in place using python's in built
# reverse function- and then to delineate words (using ' ') and reverse
# each word
def reversed_words(message):
    message.reverse()
    start_index = 0
    while start_index < len(message):
        print message
        try:
            end_index = message.index(' ', start_index) - 1
            next_index = end_index + 1
        except ValueError:
            end_index = len(message) - 1
            next_index = end_index

        while start_index < end_index:
            message[start_index], message[end_index] = message[end_index], message[start_index]
            start_index += 1
            end_index -= 1
        start_index = next_index
    return message

print reversed_words(['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l'])
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
print reversed_words(arr)
