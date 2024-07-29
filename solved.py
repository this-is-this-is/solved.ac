import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

t = int(input())
def DFS(y,x):
    visited[y][x] = True
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(4):
        if y+dy[i] <= n  and x+dx[i] <= m and y+dy[i] >= 0  and x+dx[i] >= 0:
            if visited[y+dy[i]][x+dx[i]] == False and arr[y+dy[i]][x+dx[i]] == 1:
                DFS(y+dy[i],x+dx[i])

for i in range(t):
    m, n, k= map(int,input().split())
    count = 0
    visited = [[False for _ in range(m+1)]for _ in range(n+1) ] 
    arr = [[0 for _ in range(m+1)]for _ in range(n+1) ] 
    for i in range(k):
        x, y = map(int,input().split())
        arr[y+1][x+1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if visited[i][j] == False and arr[i][j] == 1:
                DFS(i,j)
                count+=1
    print(count)