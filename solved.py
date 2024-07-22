import sys

def star(row, col, sz):
    if sz == 1:
        a[row][col] = '*'
        return
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                star(row + sz // 3 * i, col + sz // 3 * j, sz // 3)

n = int(input())
a = [[' ']*n for i in range(n)]
star(0, 0, n)

for i in range(n):
    for j in range(n):
        sys.stdout.write(a[i][j])
    sys.stdout.write('\n')
