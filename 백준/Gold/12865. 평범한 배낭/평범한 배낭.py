import sys
input = sys.stdin.readline
n, k = map(int, input().split())

val = [[0,0]]
dp = [[0] * (k+1) for i in range(n+1)]

for _ in range(n):
    val.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w,v = val[i]
        if j >= w:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[i][k])