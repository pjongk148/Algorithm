n = int(input())
if n == 1:
    print(4)
else:
    arr = [0] * (n + 1)
    arr[1] = 1
    arr[2] = 1
    for i in range(3,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    print(arr[-1] * 4 + arr[-2] * 2)