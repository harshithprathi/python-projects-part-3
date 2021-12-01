#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if(s[8]=='P'):
        a=str(int(s[0:2])+12)+s[2:-2]
        if(a[0]=='2' and a[1]=='4'):
            b="12"+s[2:-2]
            return b
        else:
            return a
    elif(s[0]=='1' and s[1]=='2' and s[8]=='A'):
        return ("00"+s[2:-2])
    else:
        return s[:-2]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
