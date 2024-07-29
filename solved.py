import sys
input = sys.stdin.readline
from heapq import heappush, heappop

arr1 = list(input())
arr1.remove('\n')
arr2 = list(input())
arr2.remove('\n')
n = len(arr1) + 1
m = len(arr2) + 1
LCS = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n - 1):
    for j in range(m - 1):
        if arr1[i] != arr2[j]:  
            LCS[1+i][1+j] = max(LCS[i][1+j], LCS[1+i][j])
        else:
            LCS[1+i][1+j] = LCS[i][j] + 1
result = []
x = m-1
y = n-1
while x > 0 and y > 0:
    if LCS[y][x] == LCS[y-1][x]:
        y -= 1
    elif LCS[y][x] == LCS[y][x-1]:
        x -= 1
    else:
        y -= 1
        x -= 1
        result.append(arr1[y])
result.reverse()
for i in result:
    print(i, end = '')
