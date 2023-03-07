n = int(input())
arr = list(map(int,input().split()))
tmp = [0]*n
result = -1001

for i in range(0,n) :
    tmp[i] = max(tmp[i-1]+arr[i],arr[i])
    result = max(tmp[i],result)

print(result)