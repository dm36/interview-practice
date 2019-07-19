def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

# we would call fib_memo(n - 1)
# we call fib_memo(n - 2)

# if the result of either of those numbers
# is pre-computed (in our mapping)- we'd just return it

# store the result away in the fibs mapping and return it!

# fib(3)
# fib(1), fib(2)
fibs = {}
def fib_memo(n):
    if n == 0 or n == 1:
        return n
    if n in fibs:
        return fibs[n]
    else:
        fibs[n] = fib_memo(n - 1) + fib_memo(n - 2)
        return fibs[n] # remember to return here!

# we'd start at 0, 1
# fib(2) = 0 + 1
# fib(3) = fib(1) + fib(2)
# fib(4) = fib(3) + fib(2)
# fib(5) = fib(4) + fib(3)

# keep track of what the fib_n-1 is
# also keep track of what the fib_n-2 is

def fib_iterative(n):
    result = [0, 1]

    for i in range(2, n+1):
        a = result[i - 1]
        b = result[i - 2]

        result.append(a + b)
    return result[n]
    
    # if n == 0 or n == 1:
    #     return n
    # # n = 2 onwards
    # else:
    #     fib_last = 1
    #     fib_last_last = 0
    #
    #     for _ in range(n - 1):
    #         fib = fib_last + fib_last_last
    #         fib_last = fib
    #         fib_last_last = fib_last
    #
    #     return fib

#      fib_memo(4)
#      |                      |
# fib_memo(3)             fib_memo(2)
#  |             |              |         |
# fib_memo(2) fib_memo(1)  fib_memo(1) fib_memo(0)

print fib(4)
print fib_memo(4)
print fib_iterative(4)
