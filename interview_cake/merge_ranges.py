# https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
# first take arr of tuples and sort by first element in each tuple

# thought would be to keep merging if the second element in the first tuple
# is less than the first element in the second tuple- i.e.

# [(0, 4), (3, 5), (4, 8), (7, 12), (9, 10)]

# [(0, 5), (4, 8), (7, 12), (9, 10)]

# [(0, 8), (7, 12), (9, 10)]

# [(0, 12), (9, 10)]

# now if both elements of the second tuple are between the elements of the first
# tuple- we just swallow it

# [(0, 12)]

def merge_ranges(arr):
    # by default sort sorts on the first element of each tuple
    arr.sort()
    print arr

    final_tuple = (arr[0][0], arr[0][1])

    for i in range(len(arr)-1):
        tuple1 = arr[i]
        tuple2 = arr[i+1]

        # [(0, 12), (9, 10)]
        # check if both the first and the second elements of the
        # second tuple are between the elements of the first tuple
        if final_tuple[0] < tuple2[0] < final_tuple[1]:
            if final_tuple[0] < tuple2[1] < tuple1[1]:
                continue

        # second element in the first tuple is
        # greater than the first element in the second tuple
        if tuple1[1] >= tuple2[0]:
            final_tuple = (final_tuple[0], tuple2[1])
            print final_tuple

    print final_tuple

# merge_ranges([(0, 4), (4, 8), (3, 5), (7, 12), (9, 10)])
print (merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
