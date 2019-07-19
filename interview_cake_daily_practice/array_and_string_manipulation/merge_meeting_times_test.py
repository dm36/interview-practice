import unittest


# Overlap if the following meeting's start time is less than the current meeting's
# end time

# Store an array of merged time ranges- and at any given point as you're iterating
# through the input- check to see if the meeting overlaps with the last meeting in your stored
# array- it does, merge- otherwise append
# def merge_ranges(meeting_ranges):
# 	meeting_ranges = sorted(meeting_ranges)
# 	merged_times = [meeting_ranges[0]]

# 	for start_time, end_time in meeting_ranges[1:]:
# 		if start_time <= merged_times[-1][1]:
# 			merged_times[-1] = (merged_times[-1][0], max(end_time, merged_times[-1][1]))
# 		else:
# 			merged_times.append((start_time, end_time))
# 	return merged_times

def merge_ranges(meeting_times):
    meeting_times.sort()
    merged_meeting_times = [meeting_times[0]]

    for start_time, end_time in meeting_times[1:]:
        last_start_time, last_end_time = merged_meeting_times[-1]

        if start_time <= last_end_time:
            merged_tuple = (last_start_time, max(last_end_time, end_time))
            merged_meeting_times[-1] = merged_tuple
        else:
            merged_meeting_times.append((start_time, end_time))

    return merged_meeting_times

# def merge_ranges(meetings):
#     # Sort by start time
#     sorted_meetings = sorted(meetings)

#     # Initialize merged_meetings with the earliest meeting
#     merged_meetings = [sorted_meetings[0]]

#     for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
#         last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

#         # If the current meeting overlaps with the last merged meeting, use the
#         # later end time of the two
#         if (current_meeting_start <= last_merged_meeting_end):
#             merged_meetings[-1] = (last_merged_meeting_start,
#                                   max(last_merged_meeting_end,
#                                       current_meeting_end))
#         else:
#             # Add the current meeting since it doesn't overlap
#             merged_meetings.append((current_meeting_start, current_meeting_end))

#     return merged_meetings

# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
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
