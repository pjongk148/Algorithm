steel = list(input())
arr = []
ans = 0
for i in range(len(steel)):
    if steel[i] == '(':
        arr.append('(')
    else:
        if steel[i-1] == '(':
            arr.pop()
            ans += len(arr)
        else:
            arr.pop()
            ans += 1
            
print(ans)