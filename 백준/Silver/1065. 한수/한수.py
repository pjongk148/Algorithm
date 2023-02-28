n = int(input())
ans = 0
for i in range(1, n + 1):
    if i < 100:
        ans += 1
    else:
        tmp = list(map(int, str(i)))
        if tmp[0] - tmp[1] == tmp[1] - tmp[2]:
            ans += 1
print(ans)