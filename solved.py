import sys
input = sys.stdin.readline

from collections import deque

send = [0,0,1,1,2,2]
receive = [1,2,0,2,0,1]

abc = list(map(int, input().split()))
visited = [[False for j in range(201)] for i in range(201)]
result = [False] * 201

def BFS():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    result[abc[2]] = True
    while queue:
        now = queue.popleft()
        a = now[0]
        b = now[1]
        c = abc[2] - a - b
        for i in range(6):
            next = [a,b,c]
            next[receive[i]] += next[send[i]]
            next[send[i]] = 0

            if next[receive[i]] > abc[receive[i]]:
                next[send[i]] = next[receive[i]] - abc[receive[i]]
                next[receive[i]] = abc[receive[i]]

            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                queue.append((next[0],next[1]))
                if next[0] == 0:
                    result[next[2]] = True
BFS()

for i in range(len(result)):
    if result[i]:
        print(i, end=' ')
        



