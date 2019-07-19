# Take an example:
# Say we have [(0, 1), (1, 3), (2, 5), (4, 6), (7, 8)] (after sort)

# Store (0, 1) so [(0, 1)]
# Modify- so [(0, 3)]
# Modify- so [(0, 5)]
# Modify- so [(0, 6)]
# Append so [(0, 6), (7, 8)]

# Since input is sorted- and we merging always with the last one-
# with this approach we will repeatedly combine meetings should there
# be an overlap
def merge_ranges(meetings):
    meetings.sort()
    merged_meetings = [meetings[0]]
    for i in range(1, len(meetings)):
        if meetings[i][0] <= merged_meetings[-1][1]:
            merged_meetings[-1] = (merged_meetings[-1][0], max(meetings[i][1], merged_meetings[-1][1]))
        else:
            merged_meetings.append(meetings[i])

    return merged_meetings

# Here- naming start and end times better with variables so don't have
# to think in terms of tuples and tuple indexes
def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings

print merge_ranges([(0, 1), (3, 5)])
print merge_ranges([(1, 3), (2, 4)])
print merge_ranges([(0, 1), (1, 3), (2, 5), (4, 6), (7, 8)])
# print merge_ranges([(0, 1), (3, 5)])
# print merge_ranges([(0, 1), (3, 5)])
