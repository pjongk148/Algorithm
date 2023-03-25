import sys
input=sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)],reverse=True)

ans = max([arr[i]*(i+1) for i in range(n)])

print(ans)