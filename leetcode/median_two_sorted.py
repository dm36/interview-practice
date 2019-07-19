# Filling final array half-way and then working from there
# def findMedianSortedArrays(nums1, nums2):
#     i = 0
#     j = 0
#     final_arr = []
#     len1 = len(nums1)
#     len2 = len(nums2)
#     lenhalf = (len1 + len2) / 2
#     while i < len1 and j < len2:
#         if len(final_arr) > (lenhalf + 1):
#             break
#         if nums1[i] <= nums2[j]:
#             final_arr.append(nums1[i])
#             i += 1
#         else:
#             final_arr.append(nums2[j])
#             j += 1
#
#     if len(final_arr) < (lenhalf + 1):
#         for _ in range(lenhalf - len(final_arr) + 1):
#             if i < len1:
#                 final_arr.append(nums1[i])
#                 i += 1
#             elif j < len2:
#                 final_arr.append(nums2[j])
#                 j += 1
#
#     print final_arr
#     if (len1 + len2) % 2:
#         return final_arr[-1]
#     else:
#         return float(final_arr[-1] + final_arr[-2]) / 2

# Filling final_arr to the brim and then working from there
def findMedianSortedArrays(nums1, nums2):
    i = 0
    j = 0
    final_arr = []
    len1 = len(nums1)
    len2 = len(nums2)
    while i < len1 and j < len2:
        if nums1[i] <= nums2[j]:
            final_arr.append(nums1[i])
            i += 1
        else:
            final_arr.append(nums2[j])
            j += 1

    if i < len1:
        for _ in range(len1 - i):
            final_arr.append(nums1[i])
            i += 1
    if j < len2:
        for _ in range(len2 - j):
            final_arr.append(nums2[j])
            j += 1

    if len(final_arr) % 2:
        median_ind = len(final_arr) / 2
        return final_arr[median_ind]
    else:
        median_ind1 = len(final_arr) / 2
        median_ind2 = median_ind1 - 1
        return float(final_arr[median_ind1] + final_arr[median_ind2]) / 2


# median should be the average of 1 and 3 or 2
# [1, 1, 1, 1, 3, 3, 3, 3]
print findMedianSortedArrays([1, 1, 3, 3], [1, 1, 3, 3])
print findMedianSortedArrays([1], [2, 3, 4, 5, 6, 8])
print findMedianSortedArrays([1, 3], [2])
print findMedianSortedArrays([1, 2], [3, 4])
