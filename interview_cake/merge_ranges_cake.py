# Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.
#
# For example, given:
#
#   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#
# your function would return:
#
#   [(0, 1), (3, 8), (9, 12)]

# Sort the input, and store an array of merged ranges-
# containing the merged ranges thus far.

# Add the first tuple in the input to this stored array
# and start with the first tuple as you iterate.

# If the starting_time in the current tuple under observation is less
# than or equal to the end_time in your stored array of tuples- merge
# the two- taking the first element of the current tuple under
# observation and the max of the second element of both-
# otherwise add the current tuple under observation to the merged array

def merged_ranges(meeting_times):
    # Add first element in meeting times to merged ranges
    meeting_times.sort()
    merged_ranges = [meeting_times[0]]

    for start_time, end_time in meeting_times[1:]:
        # If the start time is less than the last merged time's
        # end time, merge the two
        #
        # To take an example where the conditional test whould evaluate to True
        # start_time, end_time: (4, 8)
        # merged_ranges[-1]: (3, 5)
        print "Start, end: ", (start_time, end_time)
        if start_time <= merged_ranges[-1][1]:
            print (start_time, end_time)
            print (merged_ranges[-1])
            merged_time = (merged_ranges[-1][0], max(merged_ranges[-1][1], end_time))
            print "Merged time is: ", merged_time
            merged_ranges[-1] = merged_time
        else:
            merged_ranges.append((start_time, end_time))

    print merged_ranges

merged_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
