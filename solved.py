import sys
input = sys.stdin.readline
from collections import deque

def BFS(n):
    queue = deque([(n, 0)])
    
    visited = set()
    visited.add(n)
    
    while queue:
        current, operations = queue.popleft()
        
        if current == 1:
            return operations
        
        if current - 1 not in visited:
            visited.add(current - 1)
            queue.append((current - 1, operations + 1))
        
        if current % 2 == 0 and current // 2 not in visited:
            visited.add(current // 2)
            queue.append((current // 2, operations + 1))
        
        if current % 3 == 0 and current // 3 not in visited:
            visited.add(current // 3)
            queue.append((current // 3, operations + 1))

n = int(input())
print(BFS(n))
