from sys import stdin

n,m = map(int, input().split())

x = set()
for _ in range(n):
    x.add(stdin.readline().rstrip())

y = set()
for _ in range(m):
    y.add(stdin.readline().rstrip())

ans = sorted(list(x & y))
print(len(ans))
for i in ans:
    print(i)