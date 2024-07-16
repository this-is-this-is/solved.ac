import sys
input = sys.stdin.readline

def compare():
    global staticlist, prelist, count
    if(staticlist[0] <= prelist[0] and staticlist[1] <= prelist[1] and staticlist[2] <= prelist[2] and staticlist[3] <= prelist[3]):
        count+= 1

def removeChar(c):
    global prelist
    if(c == 'A'):
        prelist[0] -= 1
    elif(c == 'C'):
        prelist[1] -= 1    
    elif(c == 'G'):
        prelist[2] -= 1  
    elif(c == 'T'):
        prelist[3] -= 1

def addChar(c):
    global prelist
    if(c == 'A'):
        prelist[0] += 1
    elif(c == 'C'):
        prelist[1] += 1    
    elif(c == 'G'):
        prelist[2] += 1  
    elif(c == 'T'):
        prelist[3] += 1  
# A C G T
s, p = map(int, input().split())
arr = list(input())

staticlist = list(map(int, input().split()))
prelist = [0]*4
count = 0

for i in range(p):
    if(arr[i] == 'A'):
        prelist[0] += 1
    elif(arr[i] == 'C'):
        prelist[1] +=1
    elif(arr[i] == 'G'):
        prelist[2] +=1
    elif(arr[i] == 'T'):
        prelist[3] +=1

start = 0
end = p -1

while(end < s):
    compare()
    addChar(arr[end + 1])
    removeChar(arr[start])
    start += 1
    end += 1

print(count)