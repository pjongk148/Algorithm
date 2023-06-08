n = int(input())

cnt = 0
while n > 0:
    if n % 5 == 0:
        cnt += n // 5
        n = 0
    else:
        n -= 3
        cnt += 1
print(-1) if n < 0 else print(cnt)