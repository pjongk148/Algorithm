import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    arr = []
    n = int(input())
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    
    for idx in range(1, n):
        if idx == 1:
            arr[0][idx] += arr[1][idx - 1]
            arr[1][idx] += arr[0][idx - 1]
        else:
            arr[0][idx] += max(arr[1][idx - 1], arr[1][idx - 2])
            arr[1][idx] += max(arr[0][idx - 1], arr[0][idx - 2])
    print(max(arr[0][n - 1], arr[1][n - 1]))