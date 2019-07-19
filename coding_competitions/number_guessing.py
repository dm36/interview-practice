# number of test cases- in python3 input()
# returns a string so need to cast to an integer
t = int(input())
for _ in range(t):
    # guessing range

    # split the input by whitespace
    # and then cast each string to an integer
    a, b = map(int, input().split())

    # max number of tries for guessing
    n = int(input())

    a = a + 1
    for i in range(n):
        guess = (a + b)//2
        print (guess)

        result = input()
        if result == 'CORRECT':
            break
        if result == 'WRONG_ANSWER':
            break
        if result == 'TOO_SMALL':
            a = guess + 1
        if result == 'TOO_BIG':
            b = guess - 1

# import sys
#
# def solve(a, b):
#   m = (a + b) // 2
#   print(m)
#   sys.stdout.flush()
#   s = input()
#   if s == "CORRECT":
#     return
#   elif s == "TOO_SMALL":
#     a = m + 1
#   else:
#     b = m - 1
#   solve(a, b)
#
# T = int(input())
# for _ in range(T):
#   a, b = map(int, input().split())
#   _ = int(input())
#   solve(a + 1, b)
