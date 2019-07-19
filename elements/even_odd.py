def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A

# [1, 4, 3, 2]
# next_even = 0, next_odd = 3
# First 1 and 2 get swapped, and next_odd decrements to
# 2

# So we now have [2, 4, 3, 1], next_even = 0, next_odd = 2
# so 2 % 2 == 0, so we increment next_even so that next_even = 1

# [2, 4, 3, 1]
# 4 is even so 4 % 2 == 0- so we increment next_even
# so that next_even = 2, next_odd = 2

# next even = next_odd so we break out of the for loop

print (even_odd([1, 4, 3, 2]))
