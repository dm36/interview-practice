from collections import Counter

def find_it(seq):
    my_counter = Counter(seq)
    return [key for key, value in my_counter.items() if value % 2 == 1][0]
