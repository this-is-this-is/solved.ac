import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

def backTracking(start):
  if len(result) == m:
    for i in range(m):
      print(result[i], end=" ")
    print("")
    return

  for i in range(start,n):
    if arr[i] not in result:
        result.append(arr[i])
        backTracking(0)
        result.pop()

backTracking(0)