# Heap sort exercise - without heap sort :-)

n = int(input())
arr = list(map(int, input().split(' ')))
maxel = max(arr)
q = int(input())
for i in range(q):
    query = list(map(int,input().split(' ')))
    if len(query) == 1:
        print(maxel)
    else:
        if query[1] > maxel:
            maxel = query[1]
        
