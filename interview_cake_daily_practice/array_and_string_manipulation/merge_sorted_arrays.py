# O(m) + O(n + m (log n + m))
# copying over the second list and then sorting the
# two concatenated together

# or just O(nlogn) where n is the length of the two lists merged
# together
# def merge_lists(my_list, alices_list):
#     final_list = my_list + alices_list
#     final_list.sort()
#     return final_list

def merge_lists(my_list, alices_list):
    return sorted(my_list + alices_list)

# if both are empty would never go thorugh the while loop or the following
# for loops

# if one is empty and the other isn't would never enter the while loop
# and hit the for loop for the non-empty list
# def merge_lists(my_list, alices_list):
#     i, j = 0, 0
#     final_list = []
#     while i < len(my_list) and j < len(alices_list):
#         if my_list[i] < alices_list[j]:
#             final_list.append(my_list[i])
#             i += 1
#         else:
#             final_list.append(alices_list[j])
#             j += 1
#
#     for k in range(i, len(my_list)):
#         final_list.append(my_list[k])
#
#     for l in range(j, len(alices_list)):
#         final_list.append(alices_list[l])
#
#     return final_list

# def merge_lists(my_list, alices_list):
#     # Set up our merged_list
#     merged_list_size = len(my_list) + len(alices_list)
#     merged_list = [None] * merged_list_size
#
#     current_index_alices = 0
#     current_index_mine = 0
#     current_index_merged = 0
#     while current_index_merged < merged_list_size:
#         is_my_list_exhausted = current_index_mine >= len(my_list)
#         is_alices_list_exhausted = current_index_alices >= len(alices_list)
#         if (not is_my_list_exhausted and
#                 (is_alices_list_exhausted or
#                  my_list[current_index_mine] < alices_list[current_index_alices])):
#             # Case: next comes from my list
#             # My list must not be exhausted, and EITHER:
#             # 1) Alice's list IS exhausted, or
#             # 2) the current element in my list is less
#             #    than the current element in Alice's list
#             merged_list[current_index_merged] = my_list[current_index_mine]
#             current_index_mine += 1
#         else:
#             # Case: next comes from Alice's list
#             merged_list[current_index_merged] = alices_list[current_index_alices]
#             current_index_alices += 1
#
#         current_index_merged += 1
#
#     return merged_list

my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print (merge_lists(my_list, alices_list))
