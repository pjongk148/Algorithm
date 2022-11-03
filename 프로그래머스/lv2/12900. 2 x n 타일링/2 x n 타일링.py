def solution(n):
    if n ==1:
        return 1
    if n ==2:
        return 2
    arr = [0 for _ in range(n)]
    arr[0] = 1
    arr[1] = 2
    for i in range(2,n):
        arr[i] = (arr[i-1] + arr[i-2]) % 1000000007
    return arr[i]
    