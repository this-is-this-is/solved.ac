import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
maze = []
visited = [[False]*m for _ in range(n)]

for i in range(n):
    tmp = list(input())
    tmp.pop()
    for i in range(len(tmp)):
        tmp[i] = int(tmp[i])
    maze.append(tmp)

def BFS(a,b):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = True
    while queue:
        x1, y1 = queue.popleft()
        for i in range(4):
            x = x1 + dx[i]
            y = y1 + dy[i]
            if x >= 0 and y >=0 and x < n and y < m and maze[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                maze[x][y] = maze[x1][y1] + 1
                queue.append((x,y))

BFS(0,0)
print(maze[n-1][m-1])