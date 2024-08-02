import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input())
queue = PriorityQueue()
for i in range(n):
    s, e = map(int, input().split())
    queue.put((e,s))

count = 1
arr = [queue.get()]
while not queue.empty():
    value = queue.get()
    if arr[-1][0] > value[1]:
        continue
    else:
        arr.append(value)
        count+=1
print(count)
    
