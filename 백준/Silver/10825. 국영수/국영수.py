import sys
input = sys.stdin.readline
n= int(input())
arr = []
for i in range(n):
    tmp = input().split()
    arr.append(tmp)
arr.sort(key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in arr:
    print(i[0])