# Quick sort exercise

def partition(array, start, end):
    i = start + 1
    pivot = array[start]
    for j in range(start+1, end+1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[start], array[i-1] = array[i-1], array[start]
    return i-1

def quick_sort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quick_sort(array,start,pivot-1)
        quick_sort(array,pivot+1,end)

n = int(input())
arr = list(map(int, input().split(' ')))
quick_sort(arr, 0, n-1)
print(' '.join(str(arr)[1:-1].split(', ')))
