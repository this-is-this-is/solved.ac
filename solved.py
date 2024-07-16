import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
count = 0
for i in range(n):
    s = 0
    e = n-1
    value = arr[i]
    while(s < e):
        if(arr[s]+ arr[e] < value):
            s += 1
        elif(arr[s] + arr[e] == value):
            if(s != i and e != i):
                e -= 1
                count += 1
                break
            elif(s == i):
                s+=1
            elif(e == i):
                e-=1
        else:
            e -= 1
print(count)