def reverse_words(message):
    message.reverse()
    print message
    last_whitespace_ind = 0
    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            reverse(message, last_whitespace_ind, i - 1)
            last_whitespace_ind = i + 1

    print message

def reverse(message, i, j):
    while i < j:
        message[i], message[j] = message[j], message[i]
        i += 1
        j -= 1

reverse_words(list('thief cake'))

import unittest


def reverse_words(message):
    message.reverse()
    last_whitespace_ind = 0
    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            reverse(message, last_whitespace_ind, i - 1)
            last_whitespace_ind = i + 1

def reverse(message, i, j):
    while i < j:
        message[i], message[j] = message[j], message[i]
        i += 1
        j -= 1
# Tests

# class Test(unittest.TestCase):
#
#     def test_one_word(self):
#         message = list('vault')
#         reverse_words(message)
#         expected = list('vault')
#         self.assertEqual(message, expected)
#
#     def test_two_words(self):
#         message = list('thief cake')
#         reverse_words(message)
#         expected = list('cake thief')
#         self.assertEqual(message, expected)
#
#     def test_three_words(self):
#         message = list('one another get')
#         reverse_words(message)
#         expected = list('get another one')
#         self.assertEqual(message, expected)
#
#     def test_multiple_words_same_length(self):
#         message = list('rat the ate cat the')
#         reverse_words(message)
#         expected = list('the cat ate the rat')
#         self.assertEqual(message, expected)
#
#     def test_multiple_words_different_lengths(self):
#         message = list('yummy is cake bundt chocolate')
#         reverse_words(message)
#         expected = list('chocolate bundt cake is yummy')
#         self.assertEqual(message, expected)
#
#     def test_empty_string(self):
#         message = list('')
#         reverse_words(message)
#         expected = list('')
#         self.assertEqual(message, expected)
#
#
# unittest.main(verbosity=2)
