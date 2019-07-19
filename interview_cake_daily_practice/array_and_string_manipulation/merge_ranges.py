# Sort the input

# Build an array of merged meeting times- add the first tuple
# from the input to to this array

# Starting from the 1st tuple iterate through every meeting time
# and check to see if it can merge with the last tuple in the sorted array

# (3, 5) (4, 8)

# This would safe to merge because the start time for the second tuple is
# before the end time for the first tuple

# We want to make sure we take the max of the two end times because we could have
# something like this:

# (1, 4) (2, 3)

# We'd merge because 2 is less than 4- but we'd also take the max of 4 and 3
# so that our merged tuple becomes (1, 4)

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

print merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
