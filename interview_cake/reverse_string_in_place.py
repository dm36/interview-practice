def reverse_string(str):
    return str[::-1]

def another_reverse_string(str):
    array_of_chars = list(str)
    array_of_chars.reverse()
    return array_of_chars

# O(n) runtime and O(1) space
def reverse_string_in_place(array_of_chars):
    start_ind = 0
    end_ind = (len(array_of_chars) - 1)

    while start_ind < end_ind:
        # temp = array_of_chars[start_ind]
        # array_of_chars[start_ind] = array_of_chars[end_ind]
        # array_of_chars[end_ind] = temp

        # for swapping can also do
        array_of_chars[start_ind], array_of_chars[end_ind] = array_of_chars[end_ind], array_of_chars[start_ind]

        start_ind += 1
        end_ind -= 1
    return array_of_chars


print (reverse_string("dog"))
print (another_reverse_string("dog"))
print (reverse_string_in_place(["r", "a", "c", "e", "c", "a", "r"]))
print (reverse_string_in_place(["s", "w", "a", "g", "g", "e", "r"]))
print (reverse_string_in_place(["d", "o", "a", "g"]))
