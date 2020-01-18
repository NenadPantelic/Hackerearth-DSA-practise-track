# Heap exercise - without heap :-)

n = int(input())
mini = midi = maxi = 0
arr = []
length = 0
for i in range(n):
    x = int(input())
    arr.append(x)
    length += 1
    if i < 2:
        print(-1)
    else:
        arr.sort()
        if i > 2:
            arr[0] = arr[1]
            arr[1] = arr[2]
            arr[2] = arr[3]
            arr.pop(-1)
        
        
        print(arr[2],end=' ')
        print(arr[1],end=' ')
        print(arr[0])
