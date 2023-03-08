a, k = map(int,input().split())

cnt = 0
while a != k:
    cnt += 1
    if k % 2 != 0:
        k -= 1
    elif k % 2 == 0 and  (k / 2) >= a:
        k /= 2
    elif k / 2 < a:
        k -= 1
print(cnt)