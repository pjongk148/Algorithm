x = int(input())

arr = [0,0,1,1] + [0] * (x-3)

for i in range(4,x+1):
    tmp = arr[i-1]
    if i % 2 == 0:
        if arr[int(i/2)] < tmp:
            tmp = arr[int(i/2)]
    if i % 3 == 0:
        if arr[int(i/3)] < tmp:
            tmp = arr[int(i/3)]
    
    arr[i] = tmp + 1
print(arr[x])