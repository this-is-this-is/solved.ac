import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(sys.stdin.readline().strip())
maxq = PriorityQueue()
minq = PriorityQueue()

one = 0
for i in range(n):

    x = int(input())
    if x == 1 :
        one = 1
    if x > 0:
        maxq.put(-x)
    elif x <= 0:
        minq.put(x)

result = []
while maxq.qsize() >= 2:
    a , b = -maxq.get(),-maxq.get()
    if a != 1 and b != 1:
      result.append(a*b)
    else:
        result.append(a)
        result.append(b)
if maxq.qsize() == 1:
    result.append(-maxq.get())
      
while minq.qsize() >= 2:
    result.append(minq.get()*minq.get())
if minq.qsize() == 1:
    result.append(minq.get())

print(sum(result))
