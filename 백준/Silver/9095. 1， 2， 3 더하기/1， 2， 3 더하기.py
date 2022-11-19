def solu(n):
    if n ==1 :
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        arr = [0,1,2,4]
        for i in range(4,n+1):
            arr.append(arr[i-1] + arr[i-2] + arr[i-3])
        return arr[n]
    
for i in range(int(input())):
    print(solu(int(input())))