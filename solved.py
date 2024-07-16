import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

arr.sort()

count = 0
s = 0
e = n-1
while(s < e):
    if(arr[s] + arr[e] > m):
        e-= 1
    elif(arr[s] + arr[e] == m):
        e -= 1
        count+=1
    else:
        s +=1
print(count)
