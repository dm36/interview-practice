import unittest

def merge_lists(my_list, alices_list):
    # Combine the sorted lists into one large sorted list
    i = 0
    j = 0

    final_lst = []

    while i < len(my_list) and j < len(alices_list):
        if my_list[i] <= alices_list[j]:
            final_lst.append(my_list[i])
            i += 1
        else:
            final_lst.append(alices_list[j])
            j += 1

    if i < len(my_list):
        for ind in range(i, len(my_list)):
            final_lst.append(my_list[ind])

    if j < len(alices_list):
        for ind in range(j, len(alices_list)):
            final_lst.append(alices_list[ind])

    return final_lst


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
