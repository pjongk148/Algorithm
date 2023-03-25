n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

ans = 0
for i in range(len(arr)):
    tmp = arr[i] * (len(arr)-i)
    if tmp > ans:
        ans = tmp

print(ans)