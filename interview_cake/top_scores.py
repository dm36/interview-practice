def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
    print unsorted_scores
    print HIGHEST_POSSIBLE_SCORE

    # Build an array of length highest_possible_score with each index
    # representing the score and the value at that index representing
    # the # of numbers with that score
    num_scores = [0] * HIGHEST_POSSIBLE_SCORE

    for score in unsorted_scores:
        num_scores[score] += 1

    scores_sorted = []

    # In reverse
    for i in range(len(num_scores) - 1, -1, -1):
        # If count is greater than 0- append count
        # many of that number to the array
        if num_scores[i] > 0:
            for j in range(num_scores[i]):
                scores_sorted.append(i)

    print scores_sorted

unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100
sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
