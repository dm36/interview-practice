 # [ 'c', 'a', 'k', 'e', ' ',
 #            'p', 'o', 'u', 'n', 'd', ' ',
 #            's', 't', 'e', 'a', 'l' ] ->

 # [ 's', 't', 'e', 'a', 'l ',
 #            'p', 'o', 'u', 'n', 'd', ' ',
 #            'c', 'a', 'k', 'e']

# import unittest
# first reverse the input
# then go through it- identifying individual words and reverse those too
# def reverse_words(message):
#     final_message = ""
#     message.reverse()
#
#     last_whitespace = 0
#
#     # if the index either reaches the length of the message or corresponds to a whitespace:
#
#     # slice everything from the last observed whitespace to i (as an array)
#     # reverse the slice, update the index of the last observed whitespace and the final message
#
#     print message
#     for i in range(len(message) + 1):
#         if i == len(message) or message[i] == ' ':
#             slice = message[last_whitespace:i]
#             slice.reverse()
#             last_whitespace = i + 1
#             final_message += ''.join(slice) + ' '
#
#     message = final_message


# def reverse_words(message):
#     final_message = ""
#     message.reverse()
#
#     last_whitespace = 0
#
#     # if the index either reaches the length of the message or corresponds to a whitespace:
#
#     # slice everything from the last observed whitespace to i (as an array)
#     # reverse the slice, update the index of the last observed whitespace and the final message
#
#     print message
#     for i in range(len(message) + 1):
#         if i == len(message) or message[i] == ' ':
#             slice = message[last_whitespace:i]
#             slice.reverse()
#             last_whitespace = i + 1
#             final_message += ''.join(slice) + ' '
#
#     message = final_message

# print reverse_words( list('vault') )
# print reverse_words( list('thief cake'))
# print reverse_words( list('one another get'))
# print reverse_words( list('rat the ate cat the'))
# print reverse_words( list('yummy is cake bundt chocolate'))

# print reverse_words( [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ])

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
