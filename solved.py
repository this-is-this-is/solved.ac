import sys
input = sys.stdin.readline
from queue import PriorityQueue

V,E = map(int, input().split())
k = int(input())
distance = [sys.maxsize]*(V+1)
visited = [False]*(V+1)
arr = [[]for _ in range(V+1)]
q = PriorityQueue()

for _ in range(E):
    u,v,w = map(int, input().split())
    arr[u].append((v,w))

q.put((0,k))
distance[k] = 0

while q.qsize() > 0:
    now = q.get()
    nowV = now[1]
    if visited[nowV]:
        continue
    visited[nowV] = True
    for tmp in arr[nowV]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[nowV] + value:
            distance[next] = distance[nowV] + value
            q.put((distance[next],next))

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")

