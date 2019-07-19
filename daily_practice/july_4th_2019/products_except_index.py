import unittest

# naive solution- take product between each number
# and every other number
# def get_products_of_all_ints_except_at_index(nums):
#     if len(nums) == 0 or len(nums) == 1:
#         raise Exception("Invalid input!")
#     products = []
#     for i in range(len(nums)):
#         product = 1
#         for j in range(len(nums)):
#             if i != j:
#                 product *= nums[j]
#         products.append(product)
#
#     return products
#
# print (get_products_of_all_ints_except_at_index([1, 7, 3, 4]))
# print (get_products_of_all_ints_except_at_index([1, 2, 3]))

# https://stackoverflow.com/questions/2104782/returning-the-product-of-a-list
# def get_products_of_all_ints_except_at_index(nums):
#     final_array = []
#     product = reduce(lambda x, y: x * y, nums)
#
#     for num in nums:
#         final_array.append(product / num)
#     return final_array
#
# print (get_products_of_all_ints_except_at_index([1, 7, 3, 4]))
# print (get_products_of_all_ints_except_at_index([1, 2, 3]))

# build an array containing the product of all nums to the left of a given num
# build an array containing the product of all nums to the right of a given num
def get_products_of_all_ints_except_at_index(nums):
    if len(nums) == 0 or len(nums) == 1:
        raise Exception("Invalid input!")

    product = 1
    left_arr = [1] * len(nums)
    for i in range(len(nums)):
        left_arr[i] = (product)
        product *= nums[i]

    product = 1
    right_arr = [1] * len(nums)
    for j in range(len(nums) - 1, -1, -1):
        right_arr[j] = (product)
        product *= nums[j]

    final_arr = []
    for i in range(len(nums)):
        final_arr.append(left_arr[i] * right_arr[i])

    return final_arr

# print (get_products_of_all_ints_except_at_index([1, 7, 3, 4]))

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)
