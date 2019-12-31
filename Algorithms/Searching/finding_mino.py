# Ternary search exercise

import math 
def func(x):
    return 2 * x * x - 12 * x + 7

def find_min(start, end):
    l, r = start, end
    for i in range(35):
        l1 = (2 * l + r)/3
        l2 = (l + 2 * r)/3
        if func(l1) < func(l2):
            r = l2
        else:
            l = l1
    return math.floor(func(r))


n = int(input())
for i in range(n):
    s, e = map(int, input().split(' '))
    print(find_min(s,e))
