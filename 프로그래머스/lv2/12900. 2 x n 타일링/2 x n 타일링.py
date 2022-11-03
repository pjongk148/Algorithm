def solution(n):
    if n ==1:
        return 1
    if n ==2:
        return 2
    arr = [1,2]
    for _ in range(2,n):
        arr.append((arr[_-1] + arr[_-2]) % 1000000007)
    return arr[n-1]
    