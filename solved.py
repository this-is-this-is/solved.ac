import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
visited = [False] *(n+1)
result = [0]*(n)
arr = [[]for _ in range(n+1)]
queue = deque()

for i in range(m):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

def BFS(start):
    visited[start] = True
    queue.append(start)
    sumarr = [0]*(n+1)
    depth = 1
    while queue:
        now = queue.popleft()
        visited[now] = True
        for i in arr[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                sumarr[i] = sumarr[now] +1
    result[start-1] = sum(sumarr) 
for i in range(1, n+1):
    visited = [False] *(n+1)
    BFS(i)
print(result.index(min(result))+1)
