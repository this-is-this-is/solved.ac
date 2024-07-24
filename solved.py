import sys
input = sys.stdin.readline

count = 0
max_len = 0
k, n = map(int, input().split())
arr = []

for i in range(k):
    arr.append(int(input()))
    
start = 1
end = max(arr)   

while (start <= end):
    mid = (start+end)//2

    for i in arr:
        count += i//mid
    
    if count >= n:
        max_len = mid
        start = mid + 1
    elif count < n:
        end = mid - 1

    count = 0
    
print(max_len)
    

