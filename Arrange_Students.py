'''
A classroom has several students, half of whom are boys and half of whom are girls. You need to arrange all of them in a line for the morning assembly such that the following conditions are satisfied:

The students must be in order of non-decreasing height.
Two boys or two girls must not be adjacent to each other.
'''

import math
import os
import random
import re
import sys

#
# Complete the 'arrangeStudents' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def arrangeStudents(a, b):
    # Write your code here
    a = sorted(a)
    b = sorted(b)
    
    d = [0]*(len(a)+len(b))
    d[::2] = a
    d[1::2] = b
    e = [0]*(len(a)+len(b))
    e[::2] = b
    e[1::2] = a
    if(d == sorted(d) or e == sorted(e)): print('YES')
    else: print('NO')


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = arrangeStudents(a, b)
