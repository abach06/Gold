# Monday - Python If-Else: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    
if n%2 != 0:
    print("Weird")
else:
    if n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    else:
        print("Not Weird")
        
    #for loop
#for i in range(0, 5):
 #   print ("i")
 #print ("i")
 
 #while loop
    
#i = 0
#while i < 5:
 #    print ("i")
#i += 1  
 
 w= len(sub_string)
    count = 0
    
    for i in range(len(string)-w+1):
        window = string[i: i+w]
        if window == sub_string:
            count = count + 1
    return count   