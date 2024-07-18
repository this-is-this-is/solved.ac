import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append((int(input()),i))

sorted_arr = sorted(arr)

max = 0
for i in range(n):
    if max < sorted_arr[i][1]-i:
        max = sorted_arr[i][1]-i

print(max+1)