import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

sarr = [0]
tmp = 0
for i in arr:
    tmp += i
    sarr.append(tmp)
print(sum(sarr))