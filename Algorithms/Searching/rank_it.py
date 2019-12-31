# Binary search exercise

def binary_search(array, element, low, high):
    mid = low + (high - low)//2
    if low > high:
        return -1
    if array[mid] == element:
        return mid + 1
    elif array[mid] > element:
        return binary_search(array,element, 0, mid-1)
    else:
        return binary_search(array, element, mid+1, high)
        
n = int(input())
array = list(map(int, input().split(' ')))
array.sort()
query_num = int(input())
for i in range(query_num):
    print(binary_search(array, int(input()), 0, n-1))
