import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    arr = []
    n = int(input())
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    
    if n == 1:
        print(max(max(arr)))
        continue    
    
    arr[0][1] += arr[1][0]
    arr[1][1] += arr[0][0]
    
    for idx in range(2, n):
        arr[0][idx] += max(arr[1][idx - 1], arr[1][idx - 2])
        arr[1][idx] += max(arr[0][idx - 1], arr[0][idx - 2])
        
    print(max(arr[0][n - 1], arr[1][n - 1]))