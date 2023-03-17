n = int(input())

tmp1 = list(map(int, input().split()))
tmp2 = list(map(int, input().split()))
arr1 = sorted(tmp1, reverse=True)
arr2 = sorted(tmp2)
ans = 0

for _ in range(n):
    ans += arr1[_] * arr2[_]
print(ans)