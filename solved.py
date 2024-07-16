import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arrA = list(map(int, input().split()))
arrS = []
sum = 0
for i in arrA:
    sum += i
    arrS.append(sum)

count = 0
arrC = [0]*m

for i in range(n):
    x = arrS[i]%m
    arrC[x] += 1
    if(x == 0):
        count+=1

for i in range(m):
    if(arrC[i] > 1):
        count += (arrC[i] * (arrC[i]-1)//2) 
print(count)