# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
    # Write your code here.

fibonacci_map = {}
def fibonacci(n):
    if n == 0 or n == 1:
        return n

    if (n - 1) in fibonacci_map:
        fib_nminus1 = fibonacci_map[n-1]
    else:
        fib_nminus1 = fibonacci(n-1)

    if (n - 2) in fibonacci_map:
        fib_nminus2 = fibonacci_map[n-2]
    else:
        fib_nminus2 = fibonacci(n-2)

    return fib_nminus1 + fib_nminus2
    # Write your code here.

n = int(raw_input())
print(fibonacci(n))


n = int(raw_input())
print(fibonacci(n))
