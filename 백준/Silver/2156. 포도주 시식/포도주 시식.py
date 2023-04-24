n = int(input())

arr = [0] * 10000
for i in range(n):
    arr[i] = int(input())

cnt = [0] * 10000
cnt[0] = arr[0]
cnt[1] = arr[0] + arr[1]
cnt[2] = max(cnt[1], arr[0] + arr[2], arr[1] + arr[2])
for i in range(3,n):
    cnt[i] = max(cnt[i-2] + arr[i],cnt[i-3]+ arr[i-1] + arr[i],cnt[i-1])

print(max(cnt))