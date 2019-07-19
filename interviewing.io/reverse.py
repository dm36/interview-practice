def reverse_words(arr):
    # Convert array of characters representation to a string
    final_str = ""
    for i in range(len(arr)):
        final_str += arr[i]
    print "String: "
    print final_str
    print
    # Split on the whitespace so that we now have an array of words
    split_arr = final_str.split(" ")
    print "Array of words: "
    print split_arr
    print

    # Reverse the array of words
    split_arr.reverse()
    print "Reversed array of words: "
    print split_arr
    print

    # Convert back to an array of characters
    array_of_chars = []
    for i in range(len(split_arr)):
        for char in split_arr[i]:
            array_of_chars.append(char)
        if i != len(split_arr) - 1:
            array_of_chars.append(" ")
    print "Output: "
    print array_of_chars

# Reverse the array of chars and then reverse each word
def reverse_words_better(arr):
    arr.reverse()
    print arr

    prev_whitespace_ind = 0
    while True:
        whitespace_ind = arr.index(" ", prev_whitespace_ind + 1)
        arr[:whitespace_ind] = arr[prev_whitespace_ind:whitespace_ind][::-1]
        print arr
        prev_whitespace_ind = whitespace_ind

    whitespace_ind = arr.index(" ")
    arr[:whitespace_ind] = arr[:whitespace_ind][::-1]
    print arr

    whitespace_ind2 = arr.index(" ", whitespace_ind + 1)
    arr[whitespace_ind + 1:whitespace_ind2] = arr[whitespace_ind + 1: whitespace_ind2][::-1]
    print arr

    arr[whitespace_ind2 + 1: ] = arr[whitespace_ind2 + 1: ][::-1]
    print arr

    # temp_ind = whitespace_ind
    # temp_ind -= 1
    # i = 0
    # while i < temp_ind:
    #     temp = arr[i]
    #     arr[i] = arr[temp_ind]
    #     arr[temp_ind] = temp
    #     i += 1
    #     temp_ind -= 1
    # print arr


arr = []
str1 = "perfect"
str2 = "makes"
str3 = "practice"

for i in range(len(str1)):
    arr.append(str1[i])

arr.append(" ")

for i in range(len(str2)):
    arr.append(str2[i])

arr.append(" ")

for i in range(len(str3)):
    arr.append(str3[i])

print "Input: "
print arr

reverse_words(arr)
reverse_words_better(arr)
