import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    num = int(input())
    arr = []
    for j in range(num):
        arr.append(tuple(map(int, input().split())))
    arr.sort()
    
    tmp = arr[0][1]
    idx = 1
    for i in range(1,num):
        if arr[i][1] < tmp:
            tmp = arr[i][1]
            idx += 1
            
    print(idx)