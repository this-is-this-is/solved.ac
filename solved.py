import sys
input = sys.stdin.readline

n = int(input())
count = 1
s = 1
e = 1
sum = 1
while e < n:
    if(sum < n):
        e += 1
        sum += e
    elif(sum == n):
        e += 1
        sum += e
        count += 1
    else:
        sum -= s
        s += 1
        

print(count)