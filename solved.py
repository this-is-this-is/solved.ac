import sys
import heapq

INF = 1e8

input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 반드시 지나야하는 정점
v1, v2 = map(int, input().split())

def dijkstra(start_node):
    queue = []

    heapq.heappush(queue, [0, start_node])
    # 거리
    distances = [INF] * (n + 1)
    distances[start_node] = 0

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if distances[current_node] < current_dist:
            continue

        for i in graph[current_node]:
            if i[1] + current_dist < distances[i[0]]:
                distances[i[0]] = current_dist + i[1]
                heapq.heappush(queue, [current_dist + i[1], i[0]])

    return distances

path1 = dijkstra(1)
path2 = dijkstra(v1)
path3 = dijkstra(v2)

v1_path = path1[v1] + path2[v2] + path3[n]
v2_path = path1[v2] + path3[v1] + path2[n]

ans = min(v1_path, v2_path)

print(ans if ans < INF else -1)