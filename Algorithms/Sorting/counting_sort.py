# Counting Sort exercise

def count_array(array):
    freqs = {}
    for elem in array:
        if elem not in freqs:
            freqs[elem] = 0
        freqs[elem] += 1
    for elem in sorted(freqs.keys()):
        print(elem, end=" ")
        print(freqs[elem])

n = int(input())
arr = list(map(int, input().split(' ')))
count_array(arr)
