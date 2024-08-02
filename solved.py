import sys
input = sys.stdin.readline
import math

min, max = map(int, input().split())

check = [0]*(max-min+1)

for i in range(2, int(math.sqrt(max)+1)):
    pow = i**2
    start = int(min/pow)
    if min % pow != 0:
        start+=1
    for j in range(start, int(max/pow)+1):
        check[int(j*pow)-min] = 1

count = 0
for i in range(max-min+1):
    if check[i] == 0:
        count+=1

print(count)



    
