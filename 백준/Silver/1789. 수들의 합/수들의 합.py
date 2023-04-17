s = int(input())
ans = 0
cnt = 0
while ans <= s:
    cnt += 1
    ans += cnt
print(cnt -1)