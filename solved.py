import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())

visited = [False] * (n+1)
arr = [[] for _ in range(n+1)]

for i in range(m):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

for i in range(n+1):
    arr[i].sort()

def DFS(start):
    print(start, end = " ")
    visited[start] = True
    for i in arr[start]:
        if not visited[i]:
            DFS(i)
DFS(v)
print("")


def BFS(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        now = queue.popleft()
        print(now, end = " ")
        for i in arr[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
visited = [False] * (n+1)
BFS(v)