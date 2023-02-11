ans = set()
for _ in range(10):
    x = int(input()) % 42
    ans.add(x)
print(len(ans))