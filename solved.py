import sys
input = sys.stdin.readline

def go(a, b, c):
    if b == 1:
        return a % c
    ret = go(a, b // 2, c)
    ret = (ret * ret) % c
    if b % 2:
        ret = (ret * a) % c
    return ret

a, b, c = map(int, input().split())

print(go(a, b, c))


