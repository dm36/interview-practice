# computing an alteration, 5.8
A = [1, 2, 3, 4, 5]

for i in range(len(A)):
    print A[i:i+2]
    print sorted(A[i:i+2], reverse = i%2)
    A[i:i+2] = sorted(A[i:i+2], reverse = i%2)
print A

# so if i is even, reverse = 0, if i is odd, reverse = 1
# so if i is even sort in ascending order, if i is odd
# sort in descending order

# Swap A[i] and A[i + 1] when i is even and A[i] > A[i + 1]
# or when i is odd and A[i] < A[i+1]

# i.e. an even element should be less than the next odd element
# an odd element should be greater than the next even element
# otherwise we swap!
