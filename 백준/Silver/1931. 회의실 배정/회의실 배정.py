import sys
n = int(sys.stdin.readline())

arr = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    arr.append((start, end))


arr.sort(key = lambda x:(x[1],x[0]))

cnt = 1
tmp = arr[0]
for i in range(1,len(arr)):
    if tmp[1] <= arr[i][0]:
        cnt +=1
        tmp = arr[i]
print(cnt)