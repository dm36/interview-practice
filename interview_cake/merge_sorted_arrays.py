# O(n) time and O(n) space
def merge_lists(my_list, alices_list):
    final_lst = []
    i = 0
    j = 0
    # and because we want it to break as soon as we reach the length
    # of one list
    while i < len(my_list) and j < len(alices_list):
        if my_list[i] <= alices_list[j]:
            final_lst.append(my_list[i])
            i += 1
        else:
            final_lst.append(alices_list[j])
            j += 1

    # add all remaining elements in my list to final list
    if i < len(my_list):
        for k in range(i, len(my_list)):
            final_lst.append(my_list[k])

    # add all remaining elements in alice's list to final list
    if j < len(alices_list):
        for l in range(j, len(alices_list)):
            final_lst.append(alices_list[l])

    return final_lst

# concatenates all the elements into a single list and then sorts them

# runtime is O(n log n)- where n is the sum of the lengths of our inputs
# i.e. the runtime to sort our resulting list
def another_merge_lists(arr1, arr2):
    return sorted(arr1 + arr2)

# also heapq.merge()

my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print merge_lists(my_list, alices_list)
