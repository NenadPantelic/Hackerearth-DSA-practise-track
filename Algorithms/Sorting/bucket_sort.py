# Bucket sort exercise
from math import ceil, log

def insertion_sort(array):
    for i in range(len(array)):
        temp = array[i]
        j = i
        while j > 0 and temp < array[j-1]:
            array[j] = array[j-1]
            j = j - 1
        array[j] = temp
    
def bucket_sort(array):
    num_of_buckets = ceil(log(max(array), 2))
    buckets = [[] for i in range(num_of_buckets)]
    
    for val in array:
        num_of_ones = bin(val).count('1')
        buckets[num_of_ones].append(val)
    
    for bucket in buckets:
        insertion_sort(bucket)
        if len(bucket) != 0:
            print(' '.join(str(bucket)[1:-1].split(', ')))
    

n = int(input())
array = list(map(int, input().split(' ')))
bucket_sort(array)
