def plus_one(A):
    num = reduce(lambda x, y: (10 * x) + y, A) + 1
    return [int(i) for i in str(num)]

# 1 + (10 ** 2) + 2 + (10 ** 1) + 9 * (10 ** 0)
print (plus_one([1, 2, 9]))
