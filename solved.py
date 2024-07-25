import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [[] for _ in range(n+1)]

for i in range(n):
    tmp = list(map(int, input().split()))
    j = 1
    while True:
        if tmp[j] == -1:
            break
        arr[tmp[0]].append((tmp[j],tmp[j+1]))
        j+=2

def BFS(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        now = queue.popleft()
        for i in arr[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now] + i[1]
            
visited = [False] *(n+1)
distance = [0] * (n+1)       
BFS(1)

max_index = distance.index(max(distance))
visited = [False] *(n+1)
distance = [0] * (n+1)
BFS(max_index)

print(max(distance))
