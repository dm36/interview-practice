# iterate over the message

# check to see if we get a whitespace or we reach
# the end of the message

# if so we reverse everything from the last
# observed whitespace to this point

# doing so by looking at the index of the thing
# in the message

def reverse_words(message):
    last_whitespace_ind = 0

    for i in range(len(message) + 1):
	if i == len(message) or message[i] == '':
		reverse(message, last_whitespace_ind, i)
        	last_whitespace_ind = i + 1
		print (message)

# takes a list of characters and it reverses
# the characters in the list
# ['a', 'b', 'c'] => ['c', 'b', 'a']

def reverse(lst, i, j):
	while i < j:
		lst[i], lst[j] = lst[j], lst[i]
		i += 1
		j -= 1

# expected result is going to be 'cake thief'
# in a list of characters form-
# want it to be in-place reversal
message = list('thief cake')
reverse_words(message)
