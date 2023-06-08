n = int(input())
arr = list(map(int, input().split()))
arr = [0] +arr
ans = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1,i+1):
        ans[i] = max(ans[i], arr[j] + ans[i-j])
print(ans[n])