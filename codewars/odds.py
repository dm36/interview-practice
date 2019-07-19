from collections import Counter

def find_it(seq):
    my_counter = Counter(seq)
    return [key for key, value in my_counter.items() if value % 2 == 1][0]


def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 == 1:
            return num

print (find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
