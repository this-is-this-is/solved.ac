import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())

arr = [[]for _ in range(n+1)]
ladder = {}
snake = {}
for i in range(n):
    s,e = map(int, input().split())
    ladder[s] = e

for i in range(m):
    s,e = map(int, input().split())
    snake[s] = e
visited = [0 for _ in range(101)]

q = deque()

def BFS(v, count):
    q.append((v,count))
    visited[v] = True
    while q:
        now, cnt = q.popleft()
        for i in range(1,7):
            if now + i <= 100:
                if now + i  == 100:
                    print(cnt + 1)
                    exit(0)
                if not visited[now+i] and now+i in ladder:
                    q.append((ladder[now + i],cnt+1))
                    visited[now+i] = True
                    visited[ladder[now+i]] = True
                elif not visited[now+i] and now+i in snake:
                    q.append((snake[now + i],cnt+1))
                    visited[now+i] = True
                    visited[snake[now+i]] = True
                elif not visited[now+i]:
                    q.append((now + i,cnt+1))
                    visited[now+i] = True
BFS(1, 0)

