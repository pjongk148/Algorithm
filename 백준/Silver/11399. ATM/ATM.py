n = int(input())
arr = list(map(int,input().split()))
arr.sort()
cnt = 0

for i in range(n):
    cnt += arr[i] * (n-i)
print(cnt)