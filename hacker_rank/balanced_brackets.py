#!/bin/python

import math
import os
import random
import re
import sys

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.insert(0, x)
    def pop(self):
        return self.stack.pop(0)
    def len(self):
        return len(self.stack)

# Complete the isBalanced function below.

# Comments are examples of strings that a case would account for
def isBalanced(s):
    stack = Stack()
    for char in s:
        if char == '{' or char == '[' or char == '(':
            stack.push(char)
        if char == ')':
            # )()...
            # [)...
            if stack.len() == 0 or stack.pop() != '(':
                return "NO"
        if char == ']':
            # ][ ...
            # {]...
            if stack.len() == 0 or stack.pop() != '[':
                return "NO"
        if char == '}':
            # }}...
            # (}...
            if stack.len() == 0 or stack.pop() != '{':
                return "NO"

    # This handles strings like (((
    if stack.len() > 0:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        s = raw_input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
