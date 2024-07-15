import sys
input = sys.stdin.readline

n,q = map(int, input().split())
arr = list(map(int, input().split()))

sumarr = [0]
sum = 0

for i in arr:
    sum += i    
    sumarr.append(sum)
   
for i in range(q):
    s,e = map(int, input().split())
    print(sumarr[e] - sumarr[s-1])