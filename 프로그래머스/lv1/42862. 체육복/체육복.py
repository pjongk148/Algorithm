def solution(n, lost, reserve):
    arr = [1] * (n+2)

    for i in lost:
        arr[i] -= 1
    for j in reserve:
        arr[j] += 1
    arr[0] = 0
    arr[-1] = 0

    for i in range(1,len(arr)-1):
        print(i,arr)
        if arr[i] == 0:
            if arr[i-1] == 2:
                arr[i] =1
                arr[i-1] = 1
            elif arr[i+1] == 2:
                arr[i] = 1
                arr[i+1] = 1
    return arr.count(1) + arr.count(2)      