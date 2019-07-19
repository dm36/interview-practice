RED, WHITE, BLUE = range(3)

# black preceds white and white precedes gray
# elements less than the pivot followed
# by all elements greater than the pivot

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]

    # group elements smaller than the pivot

    # iterates through every element in the array
    for i in range(len(A)):
        # j iterates every element after i to the end of the array
        for j in range(i + 1, len(A)):
            # if the element is less than the pivot do a swap
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    # group elements larger than the pivot
    for i in reversed(range(len(A))):
        # if element is less than the pivot break
        if A[i] < pivot:
            break

        # look for a larger element- stop when we reach an element
        # less than the pivot since first pass has moved them
        # to the start of A
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break
    return A

# pivot index is 3 so A[3] = 0- so everything
print (dutch_flag_partition(3, [0, 1, 2, 0, 2, 1, 1]))
