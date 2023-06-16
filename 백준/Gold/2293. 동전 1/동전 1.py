import sys
input = sys.stdin.readline

n, k  = map(int,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

dp = [0] * (k+1)
for j in arr:
    for i in range(j,len(dp)):
        if i % j == 0:
            dp[i] += 1
        if j != 1:    
            dp[i] += dp[i-j]
            if (i-j) % j == 0 and i-j != 0:
                dp[i] -=1
print(dp[-1])