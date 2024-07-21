import sys
input = sys.stdin.readline
from collections import deque

def BFS(A, B):
    queue = deque([(A, 1)])  # (현재 숫자, 연산 횟수)
    
    while queue:
        current, operations = queue.popleft()
        
        if current == B:
            return operations
        
        if current * 2 <= B:
            queue.append((current * 2, operations + 1))
        
        if int(str(current) + '1') <= B:
            queue.append((int(str(current) + '1'), operations + 1))
    
    return -1

A, B = map(int, input().split())

print(BFS(A, B))
