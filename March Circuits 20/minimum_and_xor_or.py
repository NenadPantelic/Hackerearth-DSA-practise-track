#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:39:47 2020

@author: nenad
"""


def minxor(arr):
    arr.sort()
    minn = float("inf")
    for i in range(len(arr)-1):
        val_1 = (arr[i] & arr[i+1])
        val_2 = (arr[i] | arr[i+1])
        minn  = min(minn, val_1 ^ val_2)
    return minn

# Test 1
arr = list(range(1,6))
print(minxor(arr))
# Test 2
arr = [2,4,7]
print(minxor(arr))

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(minxor(arr))