# have one index i start at the arr of chars and the other
# index j start at the end of arr- swap characters at those indices
# and increment i and decrement j until they cross over
def reverse_string(arr_of_chars):
    i, j = 0, len(arr_of_chars) - 1
    while i < j:
        arr_of_chars[i], arr_of_chars[j] = arr_of_chars[j], arr_of_chars[i]
        i += 1
        j -= 1

arr_of_chars = ['c', 'a', 't']
reverse_string(arr_of_chars)
print arr_of_chars
