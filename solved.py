import sys
input = sys.stdin.readline

from queue import PriorityQueue

n = int(input())

myqueue = PriorityQueue()
result = []
for i in range(n):
    x = int(input())
    if x == 0:
        if myqueue.empty():
            print('0')
        else :
            print(myqueue.get()[1])
    else :
        myqueue.put((abs(x), x))
print(result)