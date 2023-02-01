import sys
r = sys.stdin.readline

N = int(r())
arr = [int(r()) for _ in range(N)]
k = [1, 1, 1, 2, 2]

for i in range(5, max(arr)):
    k.append(k[i-1]+k[i-5])

for i in arr:
    print(k[i-1])