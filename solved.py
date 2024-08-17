import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())

box= [list(map(int, input().split())) for _ in range(n)]
day = 0
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque() 

for y in range(n):
    for x in range(m):
        if box[y][x] == 1:
            queue.append([y, x])

while queue:
    y, x = queue.popleft()
    for i in range(4):
        dy, dx = dxy[i]
        if 0 <= dx + x < m and 0 <= dy + y < n:
            if box[y + dy][x + dx] == 0:
                box[y + dy][x + dx] += box[y][x] + 1
                queue.append([y + dy, x + dx])

isP = True

for y in range(n):
    if not isP:
        break
    for x in range(m):
        if box[y][x] == 0:
            isP = False
            break
        if box[y][x] > day:
            day = box[y][x]

if isP == 0:
    print(-1)
else:
    print(day - 1)