import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())

def isPrime(value):
    for i in range(2, int(value/2 + 1)):
        if value % i == 0:
            return False
    return True

def DFS(value):
    if len(str(value)) == n:
        print(value)
    else:
        for i in range(10):
            if i % 2 == 0:
                continue
            if isPrime(value*10 + i):
                DFS(value*10 + i)
            
DFS(2)
DFS(3)
DFS(5)
DFS(7)