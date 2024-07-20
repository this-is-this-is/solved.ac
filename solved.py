import sys
input = sys.stdin.readline
from collections import deque
arr = list(input())
arr.sort()
arr.reverse()
mydeque = deque()
index = 0
tmp = []
while index < len(arr) - 1:
    if index == len(arr) - 2:
        tmp.append(arr[index])
        index+=1
    elif arr[index] == arr[index + 1]:
        mydeque.appendleft(arr[index])
        mydeque.append(arr[index + 1])
        index += 2
    else :
        tmp.append(arr[index])
        index+=1
if len(tmp) > 1:
    print("I'm Sorry Hansoo")
else :
    if tmp:
      mydeque.insert(len(mydeque)//2, tmp[0])
    for i in mydeque :
      print(i, end = "")
    