# def binary_search_iterative(lst, num):
#     low, high = 0, len(lst) - 1
#     while low <= high:
#         mid = (low + high) / 2
#         if num == lst[mid]:
#             return mid
#         elif num < lst[mid]:
#             high = mid - 1
#         elif num > lst[mid]:
#             low = mid + 1
#     return -1
#
# # get the index of the number in the list
# def binary_search(lst, num):
# 	return binary_search_helper(lst, num, 0, len(lst) - 1)
#
# # get the number in the middle of the list
# # compare the number to the number in the middle
# # of the list
# # if the number is < => going left
# # if the number is > => going right
# # manifests in how we pass the indices along
# # in the recursion
#
# def binary_search_helper(lst, num, low, high):
# 	if (low > high):
# 		return -1
# 	mid = (low + high) / 2
# 	if num == lst[mid]:
# 		return mid
# 	elif num < lst[mid]:
# 		return binary_search_helper(lst, num, low, mid - 1)
# 	else:
# 		return binary_search_helper(lst, num, mid + 1, high)
#
# print (binary_search_iterative([1, 2, 3, 4, 5, 6], 6))
# print (binary_search([1, 2, 3, 4, 5, 6], 6))

import unittest


def contains(ordered_list, number):

    # Check if an integer is present in the list
	return binary_search_helper(ordered_list, number, 0, len(ordered_list) - 1)


def binary_search_helper(lst, num, low, high):
	if (low > high):
		return False
	mid = (low + high) / 2
	if num == lst[mid]:
		return True
	elif num < lst[mid]:
		return binary_search_helper(lst, num, low, mid - 1)
	else:
		return binary_search_helper(lst, num, mid + 1, high)


# Tests

class Test(unittest.TestCase):

    def test_empty_list(self):
        result = contains([], 1)
        self.assertFalse(result)

    def test_one_item_list_number_present(self):
        result = contains([1], 1)
        self.assertTrue(result)

    def test_one_item_list_number_absent(self):
        result = contains([1], 2)
        self.assertFalse(result)

    def test_small_list_number_present(self):
        result = contains([2, 4, 6], 4)
        self.assertTrue(result)

    def test_small_list_number_absent(self):
        result = contains([2, 4, 6], 5)
        self.assertFalse(result)

    def test_large_list_number_present(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
        self.assertTrue(result)

    def test_large_list_number_absent(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
        self.assertFalse(result)

    def test_large_list_number_first(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertTrue(result)

    def test_large_list_number_last(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        self.assertTrue(result)


unittest.main(verbosity=2)
