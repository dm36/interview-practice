# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    a = raw_input().split()
    b = raw_input().split()

    a = [int(x) for x in a]
    b = [int(x) for x in b]

    lst = list(product(a, b))
    final_str = ""
    for elem in lst:
        final_str += str(elem) + " "
    print final_str
