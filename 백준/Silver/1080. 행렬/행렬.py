

def change(arr,x, y):
        for i in range(x, x+3):
            for j in range(y, y+3):
                arr[i][j] = 1 - arr[i][j]

n,m = map(int, input().split())
arr1 = [list(map(int, list((input()))))  for _ in range(n)]
arr2 = [list(map(int, list((input()))))  for _ in range(n)]

    

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if arr1[i][j] != arr2[i][j]:
            change(arr1,i, j)
            cnt += 1

if arr1 != arr2:
    print(-1) 
else:
    print(cnt)