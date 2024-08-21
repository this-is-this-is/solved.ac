import sys
input = sys.stdin.readline
from queue import PriorityQueue

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

n,m = map(int, input().split())
pq = PriorityQueue()
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i

for i in range(m):
    s,e,w = map(int, input().split())
    pq.put((w,s,e))

useEdge = 0
result = 0

while useEdge < n - 1:
    w,s,e = pq.get()
    if find(s) != find(e):
        union(s,e)
        result+=w
        useEdge+=1

print(result)