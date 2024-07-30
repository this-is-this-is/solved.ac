import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000000)

def BFS(a, b):
    global goal
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque()
    queue.append((a,b))
    visited[a][b] = True
    while queue:
        nowy, nowx = queue.popleft()
        for i in range(4):
            x = nowx + dx[i]
            y = nowy + dy[i]
            if x < 0 or y < 0 or x > m - 1 or y > n - 1:
                continue
            else:
                if arr[y][x] == 1 and visited[y][x] == False:
                    visited[y][x] = True
                    queue.append((y,x))
                    result[y][x] = result[nowy][nowx] + 1

n,m = map(int, input().split())
arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


result = [[0]*m for _ in range(n)]
visited = [[False] *m for i in range(n)]
goal = (0,0)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            goal = (i,j)
BFS(goal[0],goal[1])
print(result)
for i in range(n):
    for j in range(m):
        if result[i][j] == 0 and arr[i][j] == 1:
            result[i][j] = -1
        print(result[i][j], end = ' ')
    print("")