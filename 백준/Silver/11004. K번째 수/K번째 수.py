n, k = map(int, input().split())
ans = list(map(int, input().split()))
ans.sort()
print(ans[k - 1])