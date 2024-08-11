import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
arr = [[]for _ in range(n+1)]
reverse = [[]for _ in range(n+1)]
indegree = [0] *(n+1)
result = [0]*(n+1)
count = 0
visited = [False]*(n+1)

for i in range(m):
    s,e,v = map(int, input().split())
    arr[s].append((e,v))
    reverse[e].append((s,v))
    indegree[e] += 1

startCity, endCity = map(int, input().split())

queue = deque()
queue.append(startCity)

while queue:
    now = queue.popleft()
    for next in arr[now]:
        indegree[next[0]] -= 1
        result[next[0]] = max(result[next[0]], result[now]+ next[1])
        if indegree[next[0]] == 0:
            queue.append(next[0])

queue.clear()
queue.append(endCity)
visited[endCity] = True

while queue:
    now = queue.popleft()
    for next in reverse[now]:
        if result[next[0]] + next[1] == result[now]:
            count += 1
            if not visited[next[0]]:
                visited[next[0]] = True
                queue.append(next[0])

print(result[endCity])
print(count)




