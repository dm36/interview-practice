#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
from collections import Counter

def checkMagazine(magazine, note):
    magazine_counter = (Counter(magazine))
    note_counter = (Counter(note))

    for word in note_counter:
        if word not in magazine_counter or note_counter[word] > magazine_counter[word]:
            print "No"
            return
    print "Yes"

if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)
