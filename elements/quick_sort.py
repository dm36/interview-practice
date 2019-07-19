# https://www.youtube.com/watch?v=MZaf_9IZCrc

def quick_sort(array, start, end):
    pind = 0

    # partition will split elements around pind so that all elements
    # less than pind are less than the pivot and elements greater than pind
    # are greater than the pivot

    # we then call quick sort recursively on everything to the left
    # and everything to the right of pind- repeating the partition process
    if start < end:
        pind = partition(array, start, end)
        quick_sort(array, start, pind - 1)
        quick_sort(array, pind + 1, end)

# partition elements so that everything to the left of pind is less than the pivot
# and everything to the right of pind is greater than the pivot, return pind

# also note that pind will take on the index of the pivot at the end after the last swap
def partition(array, start, end):
    pivot = array[end]
    pind = start # you don't want to set pindex to be 0, you want to set it to start

    # swap element with element at pind if element is less than the pivot
    for i in range(start, end - 1):
        if array[i] <= pivot:
            array[i], array[pind] = array[pind], array[i]
            pind += 1

    # swap the element at pind with the element at end
    array[end], array[pind] = array[pind], array[end]
    return pind

arr = [2, 1, 3, 6, 8, 5, 7, 4]
quick_sort(arr, 0, len(arr) - 1)
print arr
