# https://www.youtube.com/watch?v=TzeBrDU-JaY

# https://www.youtube.com/watch?time_continue=620&v=Nso25TkBsYI
# ^ Alternative solution employing indices- merge in this case
# would be in-place and be passed the indices of the left and right halves
# https://drive.google.com/drive/u/0/folders/11Niw9Hb5oi2ttW74wQ5KJt1S-uS3ddEo
# MergeSort (from 182 :) )
# https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort

def merge(arr1, arr2):
    # and so it breaks when one of the conditions
    # becomes false
    i, j, final_arr = 0, 0, []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            final_arr.append(arr1[i])
            i += 1
        # this should be an elif not an if
        elif arr2[j] < arr1[i]:
            final_arr.append(arr2[j])
            j += 1

    # handle remaining elements
    while i < len(arr1):
        final_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        final_arr.append(arr2[j])
        j += 1

    return final_arr

def merge_sort(input_arr):
    # need to return input_arr here!! that way the recursive
    # call gets the input_arr as its left or right
    if len(input_arr) == 1:
        return input_arr

    mid = len(input_arr) / 2

    # left arr is sorted input_arr[:mid]- returned either from the return
    # above or the return below
    left_arr = merge_sort(input_arr[:mid])
    # same goes for right_arr
    right_arr = merge_sort(input_arr[mid:])
    # call merge function above to merge the two sorted arrays
    final_arr = merge(left_arr, right_arr)
    return final_arr

input_arr = [1, 5, 4, 6, 4, 2]
print merge_sort(input_arr)

input_arr = [10, 5, 2, 1, 4]
print merge_sort(input_arr)

# print merge([1, 4, 5], [2, 3, 6])
