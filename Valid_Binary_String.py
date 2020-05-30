'''
You have been given a binary string containing only the characters "0" and "1". A binary string is considered valid if each of its substrings of at least a certain length contains at least one "1" character. Given the binary string, and the minimum length of substring, determine how many characters of the string need to be changed in order to make the binary string valid.

'''
import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER d
#

def minimumMoves(s, K):
    # Write your code here
    c = []
    count = 0
    for i in range(len(s)):
        if(s[i]=='1'):
            i+=1
            count = 0
        elif(s[i]=='0'):
            count+=1
        c.append(count)
    # print(c)
    d = []
    for i in range(len(c)-1):
        if(i!=0 and c[i]==0 and c[i-1]!=0):
            d.append(c[i-1])
    if(c[-1]!=0): d.append(c[-1])
    # print(d)
    sum = 0
    for i in range(len(d)):
        sum+=d[i]//K
    print(sum)
        

if __name__ == '__main__':
    s = input()

    d = int(input().strip())

    result = minimumMoves(s, d)
