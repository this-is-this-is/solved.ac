import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
visited1 = [[0 for _ in range(n)] for _ in range(n)]
visited2 = [[0 for _ in range(n)] for _ in range(n)]
normal = []
for i in range(n):
    normal.append(list(input()))
unnormal = copy.deepcopy(normal)

for i in range(n):
    for j in range(n):
        if unnormal[i][j] == 'G':
            unnormal[i][j] = 'R'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
count1 = 0
count2 = 0

def DFS(x, y, arr, visited):
    global cnt
    if visited[x][y] == 1:
        return
    cnt += 1
    visited[x][y] = 1
    for i in range(4):
        if 0 <= x+dx[i] <= n-1 and 0 <= y+dy[i] <= n-1:
            if arr[x][y] == arr[x + dx[i]][y + dy[i]] and visited[x + dx[i]][y + dy[i]] == 0:
                DFS(x + dx[i], y + dy[i], arr, visited)
for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            DFS(i, j, normal, visited1)
        if cnt != 0:
            count1+=1
        cnt = 0

        if visited2[i][j] == 0:
            DFS(i, j, unnormal, visited2)
        if cnt != 0:
            count2+=1
        cnt = 0

print(count1, count2)