#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 21:03:42 2020

@author: nenad
"""

#from math import floor, ceil
def balance_atoms(x,y,p,q):
    b12_rat = p*y / ( x * q)
    #print(b12_rat)
    b1 = b2 = None
    #prod = 1
    # x:y=p:q case
    if b12_rat == 1:
        b13_rat = p/x
        i = 1
        while True:
            val = b13_rat * i
            if int(val) == val:
                break
            i += 1
        #print(i)
        b3 = i
        b1 = b3 * p / x
        b2 = b1
    else:
        i = 1
        while True:
            val = b12_rat * i
            if int(val) == val:
                break
            i += 1
        b2 = i
        b1 = b2 * b12_rat
        b3 = b1 * x / p
    return int(b1), int(b2), int(b3)
            

    
    
# Test 
x,y,p,q = 2,4,3,6
b1,b2,b3 = balance_atoms(x, y, p, q)
print(b1, end=" ")
print(b2, end=" ")
print(b3)

x,y,p,q = map(int, input().split())
b1,b2,b3 = balance_atoms(x, y, p, q)
print(b1, end=" ")
print(b2, end=" ")
print(b3)