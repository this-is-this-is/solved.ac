import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
stack = []  

def backTracking(start):
    if len(stack) == m :
        for i in stack:
            print(i, end = " ")
        print("")
        return

    for i in range(start, n):
        if i < n - 1 and arr[i] == arr[i+1] :
            continue


        stack.append(arr[i])
        backTracking(i)
        stack.pop()
backTracking(0)