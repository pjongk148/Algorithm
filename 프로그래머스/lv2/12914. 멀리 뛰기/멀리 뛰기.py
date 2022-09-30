def solution(n):
    arr = [0] * (n+1)
    for i in range(n+1):
        if i<=1:
            arr[i]=i
        elif i==2:
            arr[i]=2
        else:
            arr[i]= arr[i-1] + arr[i-2]
    return arr[n] % 1234567