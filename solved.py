import sys
input = sys.stdin.readline

n,m = map(int, input().split())
trueP = list(map(int, input().split()))

T = trueP[0]
del trueP[0]

result = 0
party = [[]for _ in range(m)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(m):
    party[i] = list(map(int, input().split()))
    del party[i][0]

parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

for i in range(m):
    first = party[i][0]
    for j in range(1,len(party[i])):
        union(first,party[i][j])

for i in range(m):
    isP = True
    first = party[i][0]
    for j in range(len(trueP)):
        if find(first) == find(trueP[j]):
            isP = False
            break
    if isP:
        result+=1

print(result)


