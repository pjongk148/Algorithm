import sys
input = sys.stdin.readline
n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 1
start = arr[0] - 0.5
end = start + l
for i in range(0,n):
    if start < arr[i] < end:
        continue
    else:
        cnt += 1
        
        start = arr[i] -0.5
        end = start + l

print(cnt)