import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(start):
    visited[start] = True
    for i in arr[start]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        count+=1
        DFS(i)

print(count)
