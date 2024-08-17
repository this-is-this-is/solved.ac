import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input())
m = int(input())
distance = [sys.maxsize]*(n+1)
visited = [False]*(n+1)
arr = [[]for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int, input().split())
    arr[s].append((e,w))

s_index, e_index = map(int, input().split())

def dijkstra(start, end):
    pq = PriorityQueue()
    pq.put((0,start))
    distance[start] = 0
    while pq.qsize() > 0:
        nowNode = pq.get()
        now = nowNode[1]
        if not visited[now]:
            visited[now] = True
            for n in arr[now]:
                if not visited[n[0]] and distance[n[0]] > distance[now] + n[1]:
                    distance[n[0]] = distance[now] + n[1]
                    pq.put((distance[n[0]], n[0]))

    return distance[end]

print(dijkstra(s_index,e_index))

