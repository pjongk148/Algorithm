import sys
arr = []
n = int(sys.stdin.readline())
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for _ in range(n):
    print(arr[_])