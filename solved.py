import sys
input = sys.stdin.readline
import math
s, e = map(int, input().split())

count= 0
A = [0]*10000001

for i in range(2, len(A)):
    A[i] = i

for i in range(2,int(math.sqrt(len(A)))+1):
    if A[i] == 0:
        continue
    else:
        for j in range(i+i, len(A), i):
            A[j] = 0
for i in range(2, len(A)):
    if A[i] == 0:
        continue
    tmp = A[i]
    while A[i] <= e/tmp:
        if A[i] >= s/tmp:
            count+=1
        tmp *= A[i]
        
print(count)



    
