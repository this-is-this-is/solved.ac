import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000000)

def BFS(v, time):
    global k
    queue = deque()
    queue.append((v,time))
    visited = {}
    while queue:
        nowV, nowT = queue.popleft()
        
        if nowV == k:
            print(nowT)
            return
        
        for i in [-1,1,nowV]:
            if  nowV <= 100000 and nowV + i >= 0 and nowV + i not in visited:
                queue.append((nowV+i,nowT+1))
                visited[nowV + i] = 1

n, k = map(int,input().split())

BFS(n, 0)
