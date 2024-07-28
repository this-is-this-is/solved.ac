import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
from collections import deque

n=int(input())
visited=[False]*(n+1)
arr = [[] for _ in range(n+1)]
result=[0]*(n+1)
for i in range(n-1):
    s,e=map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)

def DFS(v):
    visited[v]=True
    for i in arr[v]:
        if not visited[i]:
            visited[i] = True
            result[i]=v
            DFS(i)
DFS(1)
for i in range(2,n+1):
    print(result[i])