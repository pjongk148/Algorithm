def solution(n):
    sum = [0] * (n+1)
    sum[0] =0
    sum[1] = 1
    for i in range(2,n+1):
        sum[i] = sum[i-1] + sum[i-2]
    return sum[n] % 1234567