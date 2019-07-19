def merge_sorted_arrays(array1, array2):
    i, j = 0, 0
    final_array = []

    # while loop to break when we reach the end
    # of one of the two arrays

    # if we had an or => while loop would keep going
    # even though we're at the end of one of the arrays

    # if we had an and => while loop breaks out the second
    # we reach the end of an array
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            final_array.append(array1[i])
            i += 1
        elif array2[j] < array1[i]:
            final_array.append(array2[j])
            j += 1

    if i < len(array1):
        final_array.extend(array1[i:])
    if j < len(array2):
        final_array.extend(array2[j:])
    return final_array

print (merge_sorted_arrays([1, 2, 11], [4, 5, 6]))
