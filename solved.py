import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
day = 0
dxyz = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]
queue = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                queue.append([z ,y, x])

while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        dz, dy, dx = dxyz[i]
        if 0 <= dx + x < m and 0 <= dy + y < n and 0 <= dz + z < h:
            if box[z + dz][y + dy][x + dx] == 0:
                box[z + dz][y + dy][x + dx] += box[z][y][x] + 1
                queue.append([z + dz,y + dy, x + dx])

isP = True

for z in range(h):
    if not isP:
        break
    for y in range(n):
        if not isP:
            break
        for x in range(m):
            if box[z][y][x] == 0:
                isP = False
                break
            if box[z][y][x] > day:
                day = box[z][y][x]

if isP == 0:
    print(-1)
else:
    print(day - 1)