import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [[]for _ in range(n+1)]
indegree = [0] *(n+1)
selfBuild = [0]*(n+1)

for i in range(1, n+1):
    inputList = list(map(int, input().split()))
    selfBuild[i] = (inputList[0])
    index = 1
    while True:
        preTemp = inputList[index]
        index+=1
        if preTemp == -1:
            break
        arr[preTemp].append(i)
        indegree[i]+=1

queue = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

result = [0]*(n+1)

while queue:
    now = queue.popleft()
    for next in arr[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now]+selfBuild[now])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1,n+1):
    print(result[i]+selfBuild[i])



