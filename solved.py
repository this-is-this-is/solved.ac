import sys
input = sys.stdin.readline

n,q = map(int, input().split())
arrA = [[0]*(n+1)]
arrS = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    arrTemp = [0] + list(map(int, input().split()))
    arrA.append(arrTemp)

for i in range(1, n+1):
    for j in range(1, n+1):
        arrS[i][j] = arrS[i-1][j] + arrS[i][j-1] - arrS[i-1][j-1] + arrA[i][j]

for i in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    result = arrS[x2][y2] - arrS[x2][y1-1] - arrS[x1-1][y2] + arrS[x1-1][y1-1]
    print(result)


