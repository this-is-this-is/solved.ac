import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n)]
visited = [False]*n
result = [0]*n
lcm = 1

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def DFS(v):
    visited[v] = True
    for i in arr[v]:
        next = i[0]
        if not visited[next]:
            result[next] = result[v]*i[2]//i[1]
            DFS(next)

for i in range(n-1):
    s, e , x, y = map(int, input().split())
    arr[s].append((e, x, y))
    arr[e].append((s, y, x))
    lcm *= (x*y)//gcd(x,y)

result[0] = lcm
DFS(0)
mgcd = result[0]

for i in range(1,n):
    mgcd = gcd(mgcd, result[i])
    
for i in result:
    print(i//mgcd, end = ' ')
    
