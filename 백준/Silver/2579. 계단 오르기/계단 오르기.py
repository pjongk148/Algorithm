n = int(input())
stair = [0]*302
for i in range(1,n+1):
    stair[i]=int(input())

arr = [0]*302
arr[1] = stair[1]
arr[2] = stair[1]+stair[2]
arr[3] = max(stair[1]+stair[3], stair[2]+stair[3])

for i in range(4, n+1):
    arr[i] = max(arr[i-3] + stair[i-1], arr[i-2]) + stair[i]

print(arr[n])