import sys
input = sys.stdin.readline

n = int(input())
arr = dict()
for _ in range(n):
    num = int(input())
    if num in arr:
        arr[num] += 1
    else:
        arr[num] = 1
ans = sorted(arr.items(),key = lambda x : (-x[1],x[0]))
print(int(ans[0][0]))