n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    
for i in range(1,n):
    arr[i][0] += arr[i-1][0]
    arr[i][-1] += arr[i-1][-1]
    for j in range(1,i):
        arr[i][j] += max(arr[i-1][j-1],arr[i-1][j])
print(max(arr[-1]))