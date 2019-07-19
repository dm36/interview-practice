fibs = {}

# O(2^n)- calls end up looking like a binary tree whose height is n
# http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/bin-tree.html
# number of nodes = 2^0 + 2^1 + 2^2 + 2^3... + 2^h = 2^(h+1) - 1
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# O(n) time, O(n) space
# def fib_memo(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         if (n - 1) in fibs:
#             fib_n_minus_1 = fibs[n-1]
#         else:
#             fib_n_minus_1 = fib_memo(n-1)
#             fibs[n-1] = fib_n_minus_1
#
#         if (n - 2) in fibs:
#             fib_n_minus_2 = fibs[n-2]
#         else:
#             fib_n_minus_2 = fib_memo(n-2)
#             fibs[n-2] = fib_n_minus_2
#
#         return fib_n_minus_1 + fib_n_minus_2

# O(n) time, O(n) space
def fib_memo(n):
    if n == 0 or n == 1:
        return n
    else:
        if n in fibs:
            return fibs[n]
        else:
            fibs_n_minus_1 = fib_memo(n-1)
            fibs_n_minus_2 = fib_memo(n-2)

            fibs[n] = fibs_n_minus_1 + fibs_n_minus_2
            
            return fibs_n_minus_1 + fibs_n_minus_2

print fib_memo(10)
print fib(10)
