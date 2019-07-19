import unittest

#   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#   [(0, 1), (3, 8), (9, 12)]

# sort the input

# idea is to have an array

# array stores all the times merged thus far

# compare the current tuple under observation to the last tuple
# in the array

# check to see if the start time in the current tuple is less
# than the end time in the last tuple in the array

# if so => merge- and that means taking the start time from the last tuple
# in the array and the max of the end time from the current tuple
# and the last tuple in the array

# otherwise append the tuple to the array

def merge_ranges(input):
    input.sort()
    array = [input[0]]

    for start, end in input[1:]:
        last_start = array[-1][0]
        last_end = array[-1][1]

        if start <= last_end:
            array[-1] = (last_start, max(last_end, end))
        else:
            array.append((start, end))

    return array

class Test(unittest.TestCase):
    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
merge_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
