# Linear search exercise
def last_occurence(array, elem):
    for i in range(len(array)-1, -1, -1):
        if array[i] == elem:
            return i+1
    return -1

n, m = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
print(last_occurence(array, m))
