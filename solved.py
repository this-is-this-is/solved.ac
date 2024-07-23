import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
arrive = False

def DFS(v, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            DFS(i, depth + 1)
    visited[v] = False
for _ in range(m):
    v1, v2 = map(int,input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

for i in range(n):
    DFS(i, 1)
    if arrive:
        break

if arrive :
    print(1)
else:
    print(0)