n = int(input())
ans = 0
arr = [[0] * 10 for _ in range(n)]
for i in range(10):
    if i == 0 :
        arr[0][i] = 0
    else:
        arr[0][i] = 1

for i in range(n-1):
    for j in range(10):
        if j == 0:
            arr[i+1][j+1] += (arr[i][j])
        elif j == 9:
            arr[i+1][j-1] += (arr[i][j])
        else:
            arr[i+1][j+1] += (arr[i][j])
            arr[i+1][j-1] += (arr[i][j])

print(sum(arr[-1]) % 1000000000)