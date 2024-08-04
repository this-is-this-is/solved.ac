import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(v):
    global isP
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            check[i] = (check[v]+1)%2
            DFS(i)
        elif check[i] == check[v]:
            isP = False
k = int(input())

for i in range(k):
    v,e = map(int,input().split())
    arr = [[] for _ in range(v+1)]
    visited = [False]*(v+1)
    check = [0]*(v+1)
    isP = True
    for j in range(e):
        start, end = map(int,input().split())
        arr[start].append(end)
        arr[end].append(start)
    
    for l in range(1, v+1):
        if isP:
            DFS(l)
        else:
            break

    if isP:
        print('YES')
    else:
        print('NO')


