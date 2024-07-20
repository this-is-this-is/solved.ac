import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))

arrSum = [0]
sum = 0
for i in range(len(arr)):
    sum += arr[i]
    arrSum.append(sum)

start = 0
end = k
max = arrSum[end] - arrSum[start]
while end <= n:
    if arrSum[end] - arrSum[start] > max:
        max = arrSum[end] - arrSum[start] 
    start+=1
    end+=1

print(max)