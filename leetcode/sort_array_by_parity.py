# list comprehension of all even elements
# list comprehension of all odd elements
# exend the first list by the second list
# def sort_array_by_parity(A):
#     evens = [num for num in A if num % 2 == 0]
#     print evens
#     odds = [num for num in A if num % 2]
#     print odds
#
#     # extend returns None and appends the contents of odds to the evens
#     # array- which is why we would return evens rather than even.extend(odds)
#
#     # https://www.geeksforgeeks.org/append-extend-python/
#     evens.extend(odds)
#     return evens

# https://www.programiz.com/python-programming/methods/list/sort

# O(n log n) time because of the sort
# def sort_array_by_parity(A):
#     A.sort(key = lambda x: x % 2)
#     return A

# O(n) to build the two arrays, O(k) to extend
# class Solution(object):
#     def sortArrayByParity(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         return [num for num in A if num % 2 == 0] + [num for num in A if num % 2 == 1]

# Two pointers one at i = 0, the other j = len(arr) - 1

# A[i] % 2, A[j] % 2

# (0, 0)
# If both evaluate to 0- this means that the even number at i is in the right place
# but not the even number at j- we would not swap, increment i and keep j the same

# (0, 1)
# If the first evaluates to 0- and the second evaluates to 1- that indicates both
# are in the right position, therefore we just increment i and decrement j

# (1, 0)
# The two elements are flipped- would swap and then increment i and then decrement j

# (1, 1)
# The odd element at j is in the right position so we decrement j, however the odd
# at i is not in the right position so we do not increment i

# Runtime is O(n), space is O(1)
def sort_array_by_parity(A):
    i, j = 0, len(A) - 1

    # Want to repeat this process until i and j cross over
    while i < j:
        if A[i] % 2 == 0 and A[j] % 2 == 0:
            i += 1
        elif A[i] % 2 == 0 and A[j] % 2 == 1:
            i += 1
            j -= 1
        elif A[i] % 2 == 1 and A[j] % 2 == 0:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        elif A[i] % 2 == 1 and A[j] % 2 == 1:
            j -= 1

    return A

# So we declare a result array of size length of N
# go through each value in A and if it's odd at it to the end
# and decrement the end index

# if the value is even add it and increment the start index
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        size = len(A)
        res = [None] * size
        start = 0
        end = size - 1
        for val in A:
            if val % 2 == 1:
                res[end] = val
                end = end -1
            else:
                res[start] = val
                start = start + 1
        return res


sort_array_by_parity([3, 1, 2, 4])

# We'll maintain two pointers i and j.
# The loop invariant is everything below i has parity 0 (ie. A[k] % 2 == 0 when k < i), and everything above j has parity 1.

# (A[i] % 2, A[j] % 2):
# If it is (0, 1), then everything is correct: i++ and j--.
# A[i] % 2 is < than A[j] % 2 meaning that an even elements
# is before the odd which is good to go

# swap if would not evaluate but the two if statements would evaluate
#
# If it is (1, 0), we swap them so they are correct, then continue.
# Odd before an even- so we want to do a swap
#
# We'd do the swap but not evaluate either of the if statements- wouldn't increment
# the i nor the j
#
# If it is (0, 0), only the i place is correct, so we i++ and continue.
#
# We know the even at the ith place is in the correct position but we can't
# say this for the number in the jth position- so no swap
#
# So swap if statement doesn't evaluate but the first if statement evaluates

# If it is (1, 1), only the j place is correct, so we j-- and continue.
# We know the odd at the jth place is in the correct position, but
# we can't say the same for the odd at the ith place

# So the if statement would evaluate to false, the swap would not happen
# and only the second of the two if statements would evaluate

class Solution(object):
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A

A = [3, 1, 2, 4]
print (sort_array_by_parity(A))
