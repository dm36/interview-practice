import unittest


def get_permutations(string):
    if len(string) == 0 or len(string) == 1:
        return set([string])

    char = string[-1]
    sub_str = string[:-1]
    sub_perms = get_permutations(sub_str)

    perms = []
    for perm in sub_perms:
        for i in range(len(perm)+1):
            perms.append(perm[:i] + char + perm[i:])

    return set(perms)


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
