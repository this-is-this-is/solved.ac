import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for y in range(n):
    for x in range(2, n):  
        if arr[y][x] == 0:  
            dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]

            if y > 0:   
                dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]
 
            if y > 0 and arr[y-1][x] == 0 and arr[y][x-1] == 0:
                dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]

result = dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2]
print(result)
