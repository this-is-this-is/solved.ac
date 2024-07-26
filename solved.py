import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)

while start <= end:
    mid = (start + end) // 2
    count = 0
    sum = 0
    for i in arr:
        if sum + i > mid:
            count+=1
            sum = 0
        sum+= i

    if sum != 0 :
        count+=1
        
    if count > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)
