#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:32:44 2020

@author: nenad
"""

from collections import defaultdict

def num_of_handshakes(n, dislikes):
    num = n * (n-1)//2
    #print(num)
    for idnum in dislikes:
       #print(dislikes[idnum])
        disl = dislikes[idnum]
        for val in disl:
            num -= 1
            idvals = dislikes.get(val, set())
            if idnum in idvals:
                idvals.remove(idnum)
        #disl.clear()
            
    #print(dislikes)
    return num
            
        
    
    
    

g = defaultdict(set)    
n = int(input())
for i in range(10):
    line = list(map(int, input().split()))
    g[line[0]] = set(line[1:])
print(num_of_handshakes(n, g))
    

#print(g)
g = {7: {1, 2, 3, 4, 5, 6, 8, 9, 11}, 1: {2, 3, 4, 5, 6, 7, 8, 10, 11}, 9: {1, 2, 3, 4, 5, 7, 8, 10, 11}, 8: {1, 2, 3, 4, 5, 6, 7, 9, 10}, 3: {1, 2, 4, 5, 6, 7, 9, 10, 11}, 5: {1, 2, 3, 4, 6, 8, 9, 10, 11}, 11: {1, 2, 3, 5, 6, 7, 8, 9, 10}, 4: {1, 2, 3, 5, 6, 7, 9, 10, 11}, 2: {1, 3, 4, 6, 7, 8, 9, 10, 11}, 10: {1, 2, 3, 4, 5, 6, 7, 8, 11}}
print(num_of_handshakes(n, g))