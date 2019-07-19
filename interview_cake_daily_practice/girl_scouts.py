def merge_lists(my_list, alice_list):
    i = 0
    j = 0

    final_lst = []

    # we want to break out of the while loop
    # once we reach the end of one of the two lists- which
    # is what explains the and
    while i < len(my_list) and j < len(alice_list):
        if my_list[i] <= alice_list[j]:
            final_lst.append(my_list[i])
            i += 1
        else:
            final_lst.append(alice_list[j])
            j += 1

    # copy over the remaining elements in my list
    if i < len(my_list):
        for ind in range(i + 1, len(my_list)):
            final_lst.append(my_list[i])
            
    # copy over the remaining elements in alice's list
    elif j < len(alice_list):
        for ind in range(j + 1, len(alice_list)):
            final_lst.append(alice_list[j])

    return final_lst

my_list = [3, 4, 6, 10, 11, 15]
alice_list = [1, 5, 8, 12, 14, 19]
print merge_lists(my_list, alice_list)
