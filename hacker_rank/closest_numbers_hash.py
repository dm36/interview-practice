from collections import defaultdict

# Set the min difference to be infinity (arbitrarily large) and create
# a default mapping of lists (the mapping maps differences to a list
# of tuples with that difference)

# For every element in the list iterate over all other
# elements in the list and take the absolute value of the difference
# between each corresponding element

# If the difference is less than the recorded minimum difference
# thus far- update the minimum difference- reset the map and
# map the difference to a list with one tuple- the elements that yielded
# that difference

# If the difference is equal to the minimum recorded difference
# add this tuple of elements to the hash map

# Only do it such
def closest_numbers_hash(arr):
    min_diff = float("inf")
    diff_hash = defaultdict(list)

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                diff = abs(arr[i] - arr[j])
                if diff < min_diff:
                    min_diff = diff
                    diff_hash = defaultdict(list)
                    if arr[i] < arr[j]:
                        diff_hash[diff] = [(arr[i], arr[j])]

                elif diff == min_diff:
                    if arr[i] < arr[j]:
                        diff_hash[diff].append((arr[i], arr[j]))

    for value in diff_hash.values():
        for tuple in value:
            print tuple[0], tuple[1]

    # tuples = [tuple for value in diff_hash.values() for tuple in value]
    # print tuples


closest_numbers_hash([6, 2, 4, 10])
