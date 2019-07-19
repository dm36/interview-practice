# https://www.youtube.com/watch?v=LPFhl65R7ww

# def median_of_two_sorted_arrays(list1, list2):
#     i, j = 0, 0
#     final_array = []
#
#     while i < len(list1) and j < len(list2):
#         if list1[i] <= list2[j]:
#             final_array.append(list1[i])
#             i += 1
#         elif list2[j] < list1[i]:
#             final_array.append(list2[j])
#             j += 1
#
#     if i < len(list1):
#         final_array.extend(list1[i:])
#     if j < len(list2):
#         final_array.extend(list2[j:])
#
#     n = len(final_array)
#     if n % 2 == 1:
#         return final_array[n / 2]
#     else:
#         first_num = final_array[(n / 2) - 1]
#         second_num = final_array[n / 2]
#         return (float((first_num + second_num)) / 2)
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# # median here is 2.5
# # 1, 2, 3, 4
#
# # length is even => take the average of the number n / 2 and the n /2 + 1
#
# # 1, 2, 3, 4, 5
# # length is odd => take the number at index n / 2
#
# print (median_of_two_sorted_arrays(nums1, nums2))

# in reality- we only need to put n / 2 elements into our array
# def median_of_two_sorted_arrays(list1, list2):
#     i, j = 0, 0
#     final_array = []
#
#     while i < len(list1) and j < len(list2):
#         if list1[i] <= list2[j]:
#             final_array.append(list1[i])
#             i += 1
#         elif list2[j] < list1[i]:
#             final_array.append(list2[j])
#             j += 1
#
#     if i < len(list1):
#         final_array.extend(list1[i:])
#     if j < len(list2):
#         final_array.extend(list2[j:])
#
#     n = len(final_array)
#     if n % 2 == 1:
#         return final_array[n / 2]
#     else:
#         first_num = final_array[(n / 2) - 1]
#         second_num = final_array[n / 2]
#
#         return (float((first_num + second_num)) / 2)

def median_of_two_sorted_arrays(list1, list2):
    my_len = len(list1) + len(list2)
    even_flag = False if my_len % 2 else True
    median_flag = False
    count = 0
    final_array = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if count == my_len / 2 + 1:
            median_flag = True
            break
        if list1[i] <= list2[j]:
            final_array.append(list1[i])
            i += 1
        elif list2[j] < list1[i]:
            final_array.append(list2[j])
            j += 1
        count += 1

    if not median_flag:
        if i < len(list1):
            while count < (my_len / 2) + 1:
                final_array.append(list1[i])
                i += 1
                count += 1
        elif j < len(list2):
            while count < (my_len / 2) + 1:
                final_array.append(list2[j])
                j += 1
                count += 1

    if even_flag:
        first_num = final_array[-1]
        second_num = final_array[-2]
        return float(first_num + second_num) / 2

    elif not even_flag:
        return final_array[-1]

# 1, 2, 3, 4, 5, 6
# 1, 2, 3, 4
print (median_of_two_sorted_arrays([1, 2], [3, 4]))

# print (median_of_two_sorted_arrays([1, 2, 3], [4, 5, 6]))
# print (median_of_two_sorted_arrays([1, 2, 3], [4, 5, 6]))
