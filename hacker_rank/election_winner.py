from collections import Counter

def electionWinner(votes):
    arr = []

    counter_votes = Counter(votes)
    max_votes = max(counter_votes.values())
    for key, val in counter_votes.items():
        if val == max_votes:
            arr.append(key)

    arr.sort()
    return arr[-1]

electionWinner(["Alex", "Michael", "Harry", "Dave", "Michael", "Victor", "Harry", "Alex", "Mary", "Mary"])
