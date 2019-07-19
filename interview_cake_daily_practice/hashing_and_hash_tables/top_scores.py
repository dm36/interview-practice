# sorted list of scores in less than O(nlogn) time
# def sort_scores(unsorted_scores, highest_possible_score):
#     unsorted_scores.sort(reverse=True)
#     print unsorted_scores

# So we can build an array of size highest_possible_score
# and update its contents with the count of each score-
# each index represents the score and the value at that index
# represents the count of numbers with that score
def sort_scores(unsorted_scores, highest_possible_score):
    sorted_scores = [0] * highest_possible_score
    for score in unsorted_scores:
        sorted_scores[score] += 1

    # get the indices that we've updated i.e. the scores
    print [ind for ind, val in enumerate(sorted_scores) if val == 1]

    for i, score in enumerate(reversed(sorted_scores)):
        if score >= 1:
            print i


sort_scores([37, 89, 41, 65, 91, 53], 100)
