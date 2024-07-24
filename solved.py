import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = sum(arr)
max_value = 0

while(start <= end):
    mid = (start + end)//2
    
    len = 0
    for i in arr:
        if i > mid:
            len += i - mid
    if len < m:
        end = mid - 1
    elif len == m:
        max_value = mid
        break
    else:
        max_value = mid
        start = mid + 1
print(max_value)

