def solution(n):
    if n == 1:
        return 0
    cnt = 0
    while cnt != 500:
        cnt += 1
        if n % 2== 0:
            n /= 2
        else:
            n = n * 3 + 1
        if n == 1:
            break
    if n != 1:
        return -1
    else:
        return cnt