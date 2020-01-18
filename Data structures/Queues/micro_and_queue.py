from collections import deque


class QueueWrapper:
    def __init__(self):
        self._queue = deque()
        self._size = 0

    def enqueue(self, elem):
        self._queue.append(elem)
        self._size += 1
        print(self._size)

    def dequeue(self):
        x = -1
        if self._size != 0:
            x =  self._queue.popleft()
            self._size -= 1

        print(x, end=" ")
        print(self._size)
        
n = int(input())
q = QueueWrapper()
for i in range(n):
    line = input().split(' ')
    if line[0] == 'E':
        q.enqueue(line[1])
    else:
        q.dequeue()
        
'''
5
E 2
D
D
E 3
D
'''
