# O((n+b)log_b(maxx))
# b - radix of digits
# Radix sort exercise

RANGE = 10
def count_sort(array, place):
    n = len(array)
    output = [0] * n
    freq = [0] * RANGE
    for i in range(n):
        digit = (array[i]//place) % RANGE
        freq[digit] += 1
    for i in range(1,RANGE):
        freq[i] += freq[i-1]

    for i in range(n-1, -1, -1):
        digit = (array[i]//place) % RANGE
        output[freq[digit]-1] = array[i]
        freq[digit] -= 1

    for i in range(n):
        array[i] = output[i]
        

def radix_sort(array):
    maxx = max(array)
    mul = 1
    while maxx:
        count_sort(array, mul)
        mul *= 10
        maxx //= 10
        print(' '.join(str(array)[1:-1].split(', ')))


    #return array

n = int(input())
array = list(map(int, input().split(' ')))
radix_sort(array)
