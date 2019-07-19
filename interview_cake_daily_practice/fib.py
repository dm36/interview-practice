# O(2^n) because it ends up looking like a binary search tree
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

# O(n), O(1) space
fibs = {}

# if the fibonacci number of a given number n has been computed
# before return it

# otherwise recurse => find fib of n - 1 and fib of n - 2
# sum those (that's our current fibonacci number), store
# that away in our fibonacci mapping so that if another
# fibonacci computation wants to use it- it can

# when we're recursing on n - 1 or n - 2, the fibonacci for these
# numbers could be stored in our mapping in which case we'd return it
# otherwise we'd repeat the process

def fib_memo(n):
    if n == 0 or n == 1:
        return n
    if n in fibs:
        return fibs[n]
    else:
        fib_n_minus_1 = fib_memo(n-1)
        fib_n_minus_2 = fib_memo(n-2)
        fibs[n] = fib_n_minus_1 + fib_n_minus_2
        return fibs[n]

print fib(0), fib(1), fib(2), fib(3), fib(4), fib(5), fib(6)
print fib_memo(0), fib_memo(1), fib_memo(2), fib_memo(3), fib_memo(4), fib_memo(5), fib_memo(6)
