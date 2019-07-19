# https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
# first take arr of tuples and sort by first element in each tuple

# if the second element in the first tuple
# is >= the first element in the second tuple, merge the two, add
# the merged tuple to our array of tuples and skip the next tuple

# if this is not the case just add the current tuple to our final array of tuples
# and keep going

# so to give an example:

# final becomes [(0, 1)] because the above property doesn't hold true
#    |
# [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]
# final = [(0, 1)]

# we add (3, 8) and then skip (4, 8) the next round
#             |
# [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]
# final = [(0, 1), (3, 8)]

# we add (9, 12) and then skip (10, 12) the next round
#                             |
# [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]
# final = [(0, 1), (3, 8), (9, 12)]

# repeat these steps until we go a pass through the arr without doing a tuple
# merge

def merge_ranges(arr):
    # by default sort sorts on the first element of each tuple
    arr.sort()

    print "Sorted array is: ", arr

    final_arr = []
    prev_arr = []
    j = 0

    merged = False
    while merged == False:
        merged = True
        final_arr = prev_arr
        skip_flag = False
        for i in range(len(arr) - 1):
            if skip_flag == True:
                merged = False
                skip_flag = False
                continue

            tuple0 = arr[i]
            tuple1 = arr[i+1]

            if tuple0[1] >= tuple1[0]:
                final_arr.append((tuple0[0], tuple1[1]))
                skip_flag = True
            else:
                final_arr.append(arr[i])

    return final_arr

print (merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
print (merge_ranges([(0, 4), (4, 8), (3, 5), (7, 12), (9, 10)]))
