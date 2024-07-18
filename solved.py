import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
myqueue = deque()

for i in range(n):
    myqueue.appendleft(i+1)

while len(myqueue) > 1 :
    myqueue.pop()
    myqueue.appendleft(myqueue.pop())

print(myqueue[0])