import sys
input = sys.stdin.readline
n, m = map(int, input().split())

result = []

def backTracking(start):
  if len(result) == m:
    for i in range(m):
      print(result[i], end=" ")
    print("")
    return

  for i in range(start,n+1):
    if i not in result:
      result.append(i)
      backTracking(i)
      result.pop()
      
backTracking(1)