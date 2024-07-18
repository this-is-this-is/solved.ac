import sys
input = sys.stdin.readline

n = int(input())
stack = []
num = 1
result = []
isP = True

for i in range(n):
    x = int(input())
    if stack and stack[-1] >= x :
        stack.pop()
        result.append("-")
    else :
        while isP :
            if stack and stack[-1] == x :
                stack.pop()
                result.append("-")
                break
            elif stack and stack[-1] > x :
                isP = False
            stack.append(num)
            num += 1
            result.append("+")
if isP :
    for i in result:
        print(i)
else :
    print("NO")