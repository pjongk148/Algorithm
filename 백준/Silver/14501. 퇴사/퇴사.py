import sys
input = sys.stdin.readline

n = int(input())
arr = [0] *(n)
for i in range(n):
    a,b = map(int, input().split())
    arr[i] = (a,b)


dp = [0] * (n+1)

for i in range(n):
    for j in range(i+arr[i][0], n+1):
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]
    
print(dp[-1])