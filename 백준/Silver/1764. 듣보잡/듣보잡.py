n,m = map(int, input().split())

x = set()
for _ in range(n):
    x.add(input())

y = set()
for _ in range(m):
    y.add(input())

ans = sorted(list(x & y))
print(len(ans))
[print(i) for i in ans]
