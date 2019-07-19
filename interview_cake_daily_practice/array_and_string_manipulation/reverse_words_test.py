import unittest

def reverse_words(message):
    message.reverse()
    i = 0

    # i iterates through the length of the message, j starts from i
    # and looks for either a whitespace or the end of the message.
    # when we find either of those two things- we save away the indices
    # don't think we can just pass i and j because our function will
    # change these indices- and pass this to our helper function
    # to reverse the string

    # make sure to break- so that the program repeats the process- sets
    # i to j + 1 so that we start after the whitespace following the
    # word we just reversed- and once again go searching for the end of the
    # word before we reverse it
    while i < len(message):
        for j in range(i, len(message) + 1):
            if j == len(message) or message[j] == ' ':
                start_ind, end_ind = i, j - 1
                reverse_string(message, start_ind, end_ind)
                break
        i = j + 1

def reverse_string(arr_of_chars, i, j):
    while i < j:
        arr_of_chars[i], arr_of_chars[j] = arr_of_chars[j], arr_of_chars[i]
        i += 1
        j -= 1

# Tests
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
