from fractions import Fraction

def plus_minus(arr):
    # First way using list comprehensions and format
    positive_nums = [x for x in arr if x > 0]
    negative_nums = [x for x in arr if x < 0]
    zero_nums = [x for x in arr if x == 0]

    print format(float(len(positive_nums)) / len(arr), '0.6f')
    print format(float(len(negative_nums)) / len(arr), '0.6f')
    print format(float(len(zero_nums)) / len(arr), '0.6f')
    print

    # Second way using a standard for loop and the fraction class
    pos = 0
    zero = 0
    neg = 0

    for elem in arr:
        if elem > 0:
            pos += 1
        if elem == 0:
            zero += 1
        if elem < 0:
            neg += 1


    a = Fraction(pos, len(arr))
    b = Fraction(neg, len(arr))
    c = Fraction(zero, len(arr))

    print format(float(a), '0.6f')
    print format(float(b), '0.6f')
    print format(float(c), '0.6f')
    print

    # Third way using a for loop and format
    print format(float(pos) / len(arr), '0.6f')
    print format(float(neg) / len(arr), '0.6f')
    print format(float(zero) / len(arr), '0.6f')

plus_minus([1, 1, 0, -1, -1])
