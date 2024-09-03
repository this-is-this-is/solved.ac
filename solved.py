import sys
input = sys.stdin.readline
from collections import deque



def BFS(v):
    global k, count, mintime
    queue = deque()
    queue.append((v, 0))  
    visited = [-1] * 100002  

    visited[v] = 0  

    while queue:
        nowV, nowT = queue.popleft()
        if nowV == k:
            if nowT < mintime:
                mintime = nowT
                count = 1
            elif nowT == mintime:
                count += 1
            continue
        for nextV in [nowV - 1, nowV + 1, nowV * 2]:
            if 0 <= nextV <= 100001:
                if visited[nextV] == -1 or visited[nextV] == nowT + 1:
                    visited[nextV] = nowT + 1
                    queue.append((nextV, nowT + 1))

n, k = map(int, input().split())
mintime = sys.maxsize 
count = 0 

BFS(n)
print(mintime)
print(count)
